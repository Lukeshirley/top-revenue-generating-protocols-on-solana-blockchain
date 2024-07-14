import requests
import pandas as pd
from sqlalchemy import create_engine

# DeFi Llama API URL for fetching protocol data
API_URL = "https://api.llama.fi/protocols"
TOP_N = 20  # Number of top protocols to fetch

def fetch_protocol_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def process_data(data):
    # Filter for Solana protocols
    solana_protocols = [protocol for protocol in data if 'Solana' in protocol['chains']]
    # Sort protocols by total revenue (fees)
    sorted_protocols = sorted(solana_protocols, key=lambda x: x['fees'], reverse=True)
    # Get top N protocols
    top_protocols = sorted_protocols[:TOP_N]
    return top_protocols

def store_data(protocols):
    # Convert to DataFrame
    df = pd.DataFrame(protocols)
    # Connect to SQLite database
    engine = create_engine('sqlite:///solana_protocols.db')
    # Store data in 'protocols' table
    df.to_sql('protocols', engine, if_exists='replace', index=False)
    print("Data successfully stored in the database.")

def main():
    data = fetch_protocol_data()
    top_protocols = process_data(data)
    store_data(top_protocols)

if __name__ == "__main__":
    main()
