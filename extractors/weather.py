import pandas as pd
import requests
from datetime import datetime, timedelta
from config.settings import SETTINGS

def extract_weather_data():
    """Extract real weather data from Open-Meteo API"""
    print("🌤️  Extracting weather data from Open-Meteo API...")
    
    all_weather_data = []
    
    for city_info in SETTINGS['cities']:
        try:
            print(f"   Fetching data for {city_info['name']}...")
            
            # Calculate date range (last 7 days)
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=7)
            
            # Build API URL
            url = "https://archive-api.open-meteo.com/v1/era5"
            params = {
                'latitude': city_info['lat'],
                'longitude': city_info['lon'],
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'hourly': 'temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation',
                'timezone': 'auto'
            }
            
            # Make API request
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            # Parse the hourly data
            hourly_data = data.get('hourly', {})
            times = hourly_data.get('time', [])
            temperatures = hourly_data.get('temperature_2m', [])
            humidity = hourly_data.get('relative_humidity_2m', [])
            wind_speeds = hourly_data.get('wind_speed_10m', [])
            precipitation = hourly_data.get('precipitation', [])
            
            # Convert to records
            for i, time_str in enumerate(times):
                if i < len(temperatures):  # Safety check
                    record = {
                        'city': city_info['name'],
                        'country': city_info['country'],
                        'latitude': city_info['lat'],
                        'longitude': city_info['lon'],
                        'timestamp': time_str,
                        'temperature_c': temperatures[i] if i < len(temperatures) else None,
                        'humidity_percent': humidity[i] if i < len(humidity) else None,
                        'wind_speed_kmh': wind_speeds[i] if i < len(wind_speeds) else None,
                        'precipitation_mm': precipitation[i] if i < len(precipitation) else None,
                        'extracted_at': datetime.now()
                    }
                    all_weather_data.append(record)
            
            print(f"   ✅ Got {len(times)} hourly records for {city_info['name']}")
            
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Failed to get data for {city_info['name']}: {e}")
            continue
        except Exception as e:
            print(f"   ❌ Error processing {city_info['name']}: {e}")
            continue
    
    df = pd.DataFrame(all_weather_data)
    print(f"✅ Total weather records extracted: {len(df)}")
    
    if len(df) > 0:
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['date'] = df['timestamp'].dt.date
        df['hour'] = df['timestamp'].dt.hour
    
    return df

def get_current_weather():
    """Get current weather for all cities (simpler version)"""
    print("🌤️  Getting current weather...")
    
    current_weather_data = []
    
    for city_info in SETTINGS['cities']:
        try:
            print(f"   Fetching current weather for {city_info['name']}...")
            
            # Use the forecast API for current conditions
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                'latitude': city_info['lat'],
                'longitude': city_info['lon'],
                'current': 'temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code',
                'timezone': 'auto'
            }
            
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            current = data.get('current', {})
            
            record = {
                'city': city_info['name'],
                'country': city_info['country'],
                'latitude': city_info['lat'],
                'longitude': city_info['lon'],
                'temperature_c': current.get('temperature_2m'),
                'humidity_percent': current.get('relative_humidity_2m'),
                'wind_speed_kmh': current.get('wind_speed_10m'),
                'weather_code': current.get('weather_code'),
                'timestamp': current.get('time'),
                'extracted_at': datetime.now()
            }
            
            current_weather_data.append(record)
            print(f"   ✅ Current weather for {city_info['name']}: {record['temperature_c']}°C")
            
        except Exception as e:
            print(f"   ❌ Error getting current weather for {city_info['name']}: {e}")
            continue
    
    df = pd.DataFrame(current_weather_data)
    return df

if __name__ == "__main__":
    # This lets you run just the weather extractor
    from utils.helpers import save_data
    
    print("Choose extraction type:")
    print("1. Historical data (last 7 days)")
    print("2. Current weather only")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "2":
        data = get_current_weather()
        save_data(data, "current_weather.csv")
    else:
        data = extract_weather_data()
        save_data(data, "raw_weather.csv")