# Weather Data Engineering Pipeline 🌤️

A simple, data engineering learning project that pulls weather data from an API, with the aim of learning about modularization.

## 🎯 Project Aim
I wanted to learn how to modularize a data pipeline end-to-end, from extraction to analytics. 
- Pull an API
- Store the API data locally
- Transform the API data 
- Quick analysis of the data 

Previously, as an Analyst, I was used to running everything in one notebook (from API pull to analysis). This project was created to help me understand the modularization process of a data engineering project.

## 📝 Design constraints
- **No data warehouse** _(Snowflake, Databricks, etc.)_
    - I decided instead to store locally, for simplicity.
- **No fancy orchestration** _(Airflow, etc.)_
    - Everything is self-contained in this project. 
- **No Data Build Tool** _(DBT, etc.)_
    - I decided to do self-contained, simple transformations within this project.

## 📊 What This Project Does

- **Extracts** real weather data from 5 major cities using the Open-Meteo API
- **Transforms** raw data with meaningful features and categories
- **Creates basic analytics** showing temperature patterns by city, time, and weather conditions


## 🏗️ Project Structure

```
weather-data-pipeline/
├── analysis/
│   └── weather_analysis.ipynb  # Jupyter notebook for basic analysis
├── config/
│   ├── __init__.py
│   └── settings.py             # Global variables
├── extractors/
│   ├── __init__.py
│   └── weather.py              # Weather API-specific extraction functions
├── utils/
│   ├── __init__.py
│   └── helpers.py              # Reusable functions
├── data/                       # Generated CSV files
├── main.py                     # Main pipeline
├── requirements.txt
├── README.md                   # ⬅️ [...You are here] 😅
└── .gitignore
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SamTaylor92/weather-data-pipeline.git
   cd weather-data-pipeline
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the pipeline**
   ```bash
   python main.py
   ```

## 📈 What You'll Get

After running the pipeline, you'll have several CSV files in the `data/` folder:

- **`raw_weather.csv`** - Raw hourly weather data from 5 cities (960+ records)
- **`clean_weather.csv`** - Transformed data with additional features
- **`analytics_weather_by_city.csv`** - Temperature statistics by city
- **`analytics_weather_by_time.csv`** - Weather patterns by time of day
- **`analytics_weather_by_day.csv`** - Weekly weather trends
- **`analytics_temperature_categories.csv`** - Hot/warm/cold analysis

## 🔍 Interactive Exploration

Open `weather_analysis.ipynb` for a basic analysis of the dataset(s):

```python
# Load weather data
weather_df = pd.read_csv('../data/clean_weather.csv')

# Convert timestamp to datetime
weather_df['timestamp'] = pd.to_datetime(weather_df['timestamp'])

print(f"📊 Dataset loaded: {len(weather_df):,} records")
print(f"🌍 Cities: {', '.join(weather_df['city'].unique())}")
print(f"📅 Date range: {weather_df['timestamp'].min().date()} to {weather_df['timestamp'].max().date()}")

# Display first few rows
weather_df.head()
```

## 🌍 Cities Included

- **Berlin, Germany** (52.52°N, 13.41°E)
- **London, UK** (51.51°N, -0.13°E)
- **New York, USA** (40.71°N, -74.01°E)
- **Tokyo, Japan** (35.68°N, 139.69°E)
- **Sydney, Australia** (-33.87°S, 151.21°E)

## 🛠️ Key Features

### 1. Data Pipeline Components
- **Extraction**: Historical weather API with error handling
- **Transformation**: Simple data cleaning, feature engineering, and categorization
- **Analytics**: Automated generation of simple business insights
- **Storage**: CSV-based data warehouse simulation

### 2. Python Best Practices (*)
- **Modular design** with clear separation of concerns
- **Proper imports** and package structure
- **Error handling** and logging
- **Virtual environment** for dependency management
- **Reusable functions** and utilities

\* _'Best practice' as my Junior Engineer mind currently understands it!_ :sweat_smile:

### 3. Learning Concepts
- **API integration** and data extraction
- **Python modularization**
- **Project organization** and code structure
- **Simple data transformations** and feature engineering
- **Interactive data exploration**

## 📊 Sample Analytics

The pipeline automatically generates insights like:

- **Hottest/coldest cities** and time periods
- **Temperature patterns** throughout the day
- **Humidity and wind speed** correlations
- **Weather categories** (hot/warm/cold) distribution
- **Precipitation patterns** by location

## 🔧 Customization

### Add More Cities
Edit `config/settings.py` to include additional cities:
```python
SETTINGS = {
    'cities': [
        {'name': 'Paris', 'lat': 48.85, 'lon': 2.35, 'country': 'France'},
        # Add more cities here
    ]
}
```

### Modify Analytics
Update the analytics functions in `main.py` to create custom insights:
```python
# Add your own analytics
weather_summary = weather_clean.groupby('your_column').agg({
    'temperature_c': ['mean', 'std'],
    'humidity_percent': 'mean'
}).round(2)
```

## 🧪 Running Individual Components

Extract weather data only:
```bash
python extractors/weather.py
```

Run specific analytics:
```bash
python -c "from main import create_weather_analytics; create_weather_analytics()"
```

## 📋 Requirements

```
requests==2.31.0
pandas==1.5.3
numpy==1.24.3
matplotlib==3.7.1
seaborn==0.12.2
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔗 API Credits

Weather data provided by [Open-Meteo](https://open-meteo.com/) - a free weather API with no authentication required.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
## 🎯 What's Next?

Potential to:
- Add database integration (SQLite, PostgreSQL)
- Implement scheduling with cron jobs or Apache Airflow
- Create a web dashboard with Flask or Streamlit
- Add data quality checks and validation
- Integrate with cloud services (AWS, GCP, Azure)
- Add more data sources (air quality, economic indicators)

---

**Built with a ❤️ for learning**

:wave: *Hey, I'm Sam! <br> <br>I'm just a Junior Data Engineer, who's documenting his way through his data-engineering journey: one concept at a time. <br><br>Feel free to give feedback and tips!* :books: :nerd_face: