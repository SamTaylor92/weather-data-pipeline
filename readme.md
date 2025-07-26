# Weather Data Engineering Pipeline 🌤️

A simple, educational data engineering project that demonstrates real-world data pipeline concepts using Python, APIs, and data analysis. Perfect for learning how data flows from extraction to analytics.

## 📊 What This Project Does

- **Extracts** real weather data from 5 major cities using the Open-Meteo API
- **Transforms** raw data with meaningful features and categories
- **Creates analytics** showing temperature patterns by city, time, and weather conditions
- **Demonstrates** professional Python project structure and data engineering best practices

## 🏗️ Project Structure

```
weather-data-pipeline/
├── config/
│   ├── __init__.py
│   └── settings.py          # Configuration and city coordinates
├── extractors/
│   ├── __init__.py
│   └── weather.py           # Weather API extraction logic
├── utils/
│   ├── __init__.py
│   └── helpers.py           # Shared utility functions
├── data/                    # Generated data files (CSV)
├── main.py                  # Main pipeline orchestration
├── explore.py               # Interactive data exploration
├── requirements.txt         # Python dependencies
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

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

Open `explore.py` or create a Jupyter notebook to interactively analyze your data:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load weather data
weather_df = pd.read_csv('./data/clean_weather.csv')

# Create visualizations
weather_df.boxplot(column='temperature_c', by='city', figsize=(12, 6))
plt.title('Temperature Distribution by City')
plt.show()
```

## 🌍 Cities Included

- **Berlin, Germany** (52.52°N, 13.41°E)
- **London, UK** (51.51°N, -0.13°E)
- **New York, USA** (40.71°N, -74.01°E)
- **Tokyo, Japan** (35.68°N, 139.69°E)
- **Sydney, Australia** (-33.87°S, 151.21°E)

## 🛠️ Key Features

### Data Pipeline Components
- **Extraction**: Real-time weather API integration with error handling
- **Transformation**: Data cleaning, feature engineering, and categorization
- **Analytics**: Automated generation of business insights
- **Storage**: CSV-based data warehouse simulation

### Python Best Practices
- **Modular design** with clear separation of concerns
- **Proper imports** and package structure
- **Error handling** and logging
- **Virtual environment** for dependency management
- **Reusable functions** and utilities

### Learning Concepts
- **API integration** and data extraction
- **Pandas** data manipulation and analysis
- **Data transformations** and feature engineering
- **Project organization** and code structure
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
faker==19.6.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📚 Learning Resources

This project demonstrates concepts similar to:
- **Databricks** - Data processing and analytics
- **dbt** - Data transformation and modeling
- **Airflow** - Pipeline orchestration
- **Looker** - Business intelligence and visualization

## 🔗 API Credits

Weather data provided by [Open-Meteo](https://open-meteo.com/) - a free weather API with no authentication required.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 What's Next?

- Add database integration (SQLite, PostgreSQL)
- Implement scheduling with cron jobs or Apache Airflow
- Create a web dashboard with Flask or Streamlit
- Add data quality checks and validation
- Integrate with cloud services (AWS, GCP, Azure)
- Add more data sources (air quality, economic indicators)

---

**Built with ❤️ for learning data engineering concepts**

*Perfect for junior data engineers, analysts transitioning to engineering roles, or anyone wanting to understand modern data pipelines.*