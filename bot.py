import requests
import pandas as pd
import time
import logging

# Configure Logging
logging.basicConfig(filename='market_data.log', level=logging.INFO)

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

def fetch_market_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            logging.error(f"API Error: {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Connection Error: {e}")
        return None

def analyze_data(data):
    # Example: Simple DataFrame manipulation
    df = pd.DataFrame(data)
    print(f"Current Prices:\n{df}")
    logging.info(f"Data Logged: {data}")

if __name__ == "__main__":
    print("Starting Market Bot...")
    while True:
        market_data = fetch_market_data()
        if market_data:
            analyze_data(market_data)
        
        # Run every 10 minutes
        time.sleep(600)