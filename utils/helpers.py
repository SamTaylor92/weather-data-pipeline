import pandas as pd
import json
import os

def save_data(data, filename):
    """Save data to CSV file"""
    filepath = f"./data/{filename}"
    data.to_csv(filepath, index=False)
    print(f"✅ Saved {len(data)} records to {filepath}")

def load_data(filename):
    """Load data from CSV file"""
    filepath = f"./data/{filename}"
    if os.path.exists(filepath):
        data = pd.read_csv(filepath)
        print(f"📖 Loaded {len(data)} records from {filepath}")
        return data
    else:
        print(f"❌ File not found: {filepath}")
        return pd.DataFrame()

def print_summary(data, title):
    """Print a nice summary of the data"""
    print(f"\n📊 {title}")
    print("=" * 40)
    print(f"Rows: {len(data)}")
    print(f"Columns: {list(data.columns)}")
    if len(data) > 0:
        print("\nFirst 3 rows:")
        print(data.head(3).to_string())
    print()