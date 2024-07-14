import requests
import pandas as pd
from sqlalchemy import create_engine

# Function to fetch protocol data from DeFi Llama API
def fetch_protocol_data():
    url = "https://api.llama.fi/protocols"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.json()

# Process the data to get the top 20 protocols by revenue/fees
def process_data(data):
    solana_protocols = [protocol for protocol in data if 'Solana' in protocol['chains']]
    # Sort by revenue or fees if available
    sorted_protocols = sorted(solana_protocols, key=lambda x: x.get('revenue', 0), reverse=True)
    # Take the top 20
    top_protocols = sorted_protocols[:20]
    return top_protocols

# Store the data in SQLite database
def store_data(protocols):
    if protocols:
        df = pd.DataFrame(protocols)
        engine = create_engine('sqlite:///solana_protocols.db')
        df.to_sql('protocols', engine, if_exists='replace', index=False, dtype={
            'id': 'INTEGER',
            'name': 'TEXT',
            'address': 'TEXT',
            'symbol': 'TEXT',
            'url': 'TEXT',
            'description': 'TEXT',
            'chain': 'TEXT',
            'logo': 'TEXT',
            'audits': 'TEXT',
            'audit_note': 'TEXT',
            'gecko_id': 'TEXT',
            'cmcId': 'TEXT',
            'category': 'TEXT',
            'chains': 'TEXT',
            'module': 'TEXT',
            'twitter': 'TEXT',
            'forkedFrom': 'TEXT',
            'oracles': 'TEXT',
            'listedAt': 'INTEGER',
            'methodology': 'TEXT',
            'slug': 'TEXT',
            'revenue': 'REAL',
            'fees': 'REAL'
        })
    else:
        print("No protocols found to store in the database.")

# Main function to fetch, process, and store data
def main():
    data = fetch_protocol_data()
    top_protocols = process_data(data)
    store_data(top_protocols)
    print("Data successfully fetched, processed, and stored in the database.")

if __name__ == "__main__":
    main()



