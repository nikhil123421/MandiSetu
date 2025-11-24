import requests
import pandas as pd
import datetime

# API Key Configuration
API_KEY = "579b464db66ec23bdd000001ea86437c4fd544a4603c57ddf42a5a2f" 

def normalize_columns(df):
    """
    Smartly renames columns to standard names.
    """
    rename_map = {
        # 1. JSON API Format 
        "market": "Market",
        "district": "District",
        "state": "State",         
        "commodity": "Commodity", 
        "modal_price": "Modal Price",
        "min_price": "Min Price",
        "max_price": "Max Price",
        "arrival_date": "Date",
        
        # 2. CSV / Excel Format
        "State": "State",
        "District": "District",
        "Market": "Market",
        "Commodity": "Commodity",
        "Arrival_Date": "Date",
        "Arrival Date": "Date",
        "Modal_x0020_Price": "Modal Price",
        "Min_x0020_Price": "Min Price",
        "Max_x0020_Price": "Max Price"
    }
    return df.rename(columns=rename_map)

def fetch_mandi_data(state, commodity):
    print(f"📡 Connecting to Govt API for {commodity} in {state}...")
    return get_live_data(state, commodity)

def get_live_data(state, commodity):
    base_url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    params = {
        "api-key": API_KEY,
        "format": "json",
        "offset": 0,
        "limit": 10000, 
        "filters[state]": state,      
        "filters[commodity]": commodity 
    }

    try:
        response = requests.get(base_url, params=params, timeout=20) 
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        raise Exception(f"Network Error: {e}")

    data = response.json()
    records = data.get("records", [])
    
    if not records:
        raise ValueError("No data found for this query")

    # 1. Create DataFrame & Use Normalize Function that we made
    df = pd.DataFrame(records)
    df = normalize_columns(df)

    if "State" in df.columns:
        df = df[df["State"].astype(str).str.strip().str.lower() == state.strip().lower()]
    
    if df.empty:
        raise ValueError(f"No data found for {state} (API Filter Mismatch)")

    # 2. Convert Prices to Numbers
    cols_to_fix = ["Modal Price", "Min Price", "Max Price"]
    for col in cols_to_fix:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # 3. Drop invalid rows
    df = df.dropna(subset=["Modal Price"])
    
    print(f"✅ Data Fetched! Found {len(df)} valid records for {state}.")
    
    return df[["Market", "District", "Modal Price", "Min Price", "Max Price", "Date"]].copy()
