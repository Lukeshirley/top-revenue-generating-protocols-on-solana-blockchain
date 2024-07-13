import requests
import pandas as pd
from sqlalchemy import create_engine

# Example API call (replace with actual API endpoint and parameters)
response = requests.get('https://api.solanabeach.io/v1/protocols')
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

# Connect to SQL database
engine = create_engine('sqlite:///solana_protocols.db')
df.to_sql('protocols', engine, if_exists='replace', index=False)
