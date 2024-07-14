import requests
import pandas as pd
from sqlalchemy import create_engine
from config import DEFI_LLAMA_API_KEY

# Function to fetch data from DeFi Llama API
def fetch_data():
    url = "https://api.llama.fi/overview/fees/revenue/solana"
    headers = {
        'x-api-key': DEFI_LLAMA_API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

# Process the data to get the top 20 protocols by revenue/fees
def process_data(data):
    protocols = data.get('protocols', [])
    solana_protocols = [protocol for protocol in protocols if 'Solana' in protocol['chains']]
    
    # Sort by revenue or fees
    sorted_protocols = sorted(solana_protocols, key=lambda x: x.get('revenue', 0), reverse=True)
    
    # Take the top 20
    top_protocols = sorted_protocols[:20]
    
    return top_protocols

# Store the data in SQLite database
def store_data(protocols):
    df = pd.DataFrame(protocols)
    engine = create_engine('sqlite:///solana_protocols.db')
    df.to_sql('protocols', engine, if_exists='replace', index=False)

# Main function to fetch, process, and store data
def main():
    data = fetch_data()
    top_protocols = process_data(data)
    store_data(top_protocols)
    print("Data successfully fetched, processed, and stored in the database.")

if __name__ == "__main__":
    main()

