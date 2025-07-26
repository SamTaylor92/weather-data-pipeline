"""
Weather-only data pipeline
"""
import os
import pandas as pd
from extractors.weather import extract_weather_data
from utils.helpers import save_data, load_data, print_summary

def transform_weather_data(raw_data):
    """Transform weather data with useful features"""
    print("🔄 Transforming weather data...")
    
    df = raw_data.copy()
    
    if 'temperature_c' in df.columns:
        # Temperature categories
        df['temp_category'] = df['temperature_c'].apply(
            lambda x: 'Cold' if pd.isna(x) or x < 10 else 'Warm' if x < 25 else 'Hot'
        )
        
        # Weather conditions
        df['high_humidity'] = df['humidity_percent'] > 70
        df['windy'] = df['wind_speed_kmh'] > 15
        df['rainy'] = df['precipitation_mm'] > 0.1
        
        # Time-based features
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['date'] = df['timestamp'].dt.date
            df['hour'] = df['timestamp'].dt.hour
            df['day_of_week'] = df['timestamp'].dt.day_name()
            df['is_weekend'] = df['timestamp'].dt.weekday >= 5
            df['time_of_day'] = df['timestamp'].dt.hour.apply(
                lambda x: 'Morning' if 6 <= x < 12 else 'Afternoon' if 12 <= x < 18 else 'Evening' if 18 <= x < 22 else 'Night'
            )
    
    print(f"✅ Transformed {len(df)} weather records")
    return df

def create_weather_analytics():
    """Create weather analytics"""
    print("📈 Creating weather analytics...")
    
    weather_clean = load_data("clean_weather.csv")
    
    if len(weather_clean) == 0:
        print("❌ No clean weather data found")
        return
    
    print("   Creating weather analytics...")
    
    # 1. Weather by city
    weather_by_city = weather_clean.groupby('city').agg({
        'temperature_c': ['mean', 'min', 'max'],
        'humidity_percent': 'mean',
        'wind_speed_kmh': 'mean',
        'precipitation_mm': 'sum',
        'timestamp': 'count'
    }).round(2)
    
    weather_by_city.columns = ['avg_temp', 'min_temp', 'max_temp', 'avg_humidity', 'avg_wind_speed', 'total_precipitation', 'data_points']
    save_data(weather_by_city.reset_index(), "analytics_weather_by_city.csv")
    
    # 2. Weather by time of day
    if 'time_of_day' in weather_clean.columns:
        weather_by_time = weather_clean.groupby('time_of_day').agg({
            'temperature_c': 'mean',
            'humidity_percent': 'mean',
            'wind_speed_kmh': 'mean',
            'timestamp': 'count'
        }).round(2)
        weather_by_time.columns = ['avg_temp', 'avg_humidity', 'avg_wind_speed', 'data_points']
        save_data(weather_by_time.reset_index(), "analytics_weather_by_time.csv")
    
    # 3. Weather by day of week
    if 'day_of_week' in weather_clean.columns:
        weather_by_day = weather_clean.groupby('day_of_week').agg({
            'temperature_c': 'mean',
            'humidity_percent': 'mean',
            'precipitation_mm': 'sum'
        }).round(2)
        weather_by_day.columns = ['avg_temp', 'avg_humidity', 'total_precipitation']
        save_data(weather_by_day.reset_index(), "analytics_weather_by_day.csv")
    
    # 4. Temperature categories summary
    if 'temp_category' in weather_clean.columns:
        temp_summary = weather_clean.groupby('temp_category').agg({
            'city': 'count',
            'humidity_percent': 'mean',
            'wind_speed_kmh': 'mean'
        }).round(2)
        temp_summary.columns = ['record_count', 'avg_humidity', 'avg_wind_speed']
        save_data(temp_summary.reset_index(), "analytics_temperature_categories.csv")

def main():
    """Run the weather data pipeline"""
    print("🌤️  Starting Weather Data Pipeline")
    print("=" * 50)
    
    # Create data folder
    os.makedirs("data", exist_ok=True)
    
    # Step 1: Extract weather data
    print("\n1️⃣ EXTRACTION")
    weather_raw = extract_weather_data()
    save_data(weather_raw, "raw_weather.csv")
    
    # Step 2: Transform weather data
    print("\n2️⃣ TRANSFORMATION")
    weather_clean = transform_weather_data(weather_raw)
    save_data(weather_clean, "clean_weather.csv")
    
    # Step 3: Create analytics
    print("\n3️⃣ ANALYTICS")
    create_weather_analytics()
    
    # Step 4: Show results
    print("\n4️⃣ RESULTS")
    print_summary(weather_clean, "Clean Weather Data")
    
    # Display analytics
    analytics_files = [
        ("analytics_weather_by_city.csv", "Weather by City"),
        ("analytics_weather_by_time.csv", "Weather by Time of Day"),  
        ("analytics_weather_by_day.csv", "Weather by Day of Week"),
        ("analytics_temperature_categories.csv", "Temperature Categories")
    ]
    
    for filename, title in analytics_files:
        data = load_data(filename)
        if len(data) > 0:
            print_summary(data, title)
    
    print("\n🎉 Weather pipeline completed successfully!")
    print("📁 Files created:")
    print("   📄 raw_weather.csv - Raw weather data from API")
    print("   📄 clean_weather.csv - Transformed weather data")
    print("   📊 analytics_weather_by_city.csv - Temperature/humidity by city")
    print("   📊 analytics_weather_by_time.csv - Patterns by time of day")
    print("   📊 analytics_weather_by_day.csv - Weekly weather patterns")
    print("   📊 analytics_temperature_categories.csv - Hot/warm/cold analysis")

if __name__ == "__main__":
    main()