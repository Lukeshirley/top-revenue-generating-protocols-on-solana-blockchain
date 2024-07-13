import requests  # Importing the requests library to make HTTP requests
import pandas as pd  # Importing pandas for data manipulation
from sqlalchemy import create_engine  # Importing create_engine from SQLAlchemy to handle SQL database connections
from config import DUNE_API_KEY  # Importing the API key from config.py

# Example SQL query to fetch data from Dune Analytics (replace with actual query)
query = """
SELECT protocol, SUM(revenue) as total_revenue
FROM solana_revenue_table
GROUP BY protocol
ORDER BY total_revenue DESC
LIMIT 10
"""

# Making a POST request to the Dune Analytics API
url = 'https://api.dune.xyz/v1/query'
headers = {
    'Authorization': f'Bearer {DUNE_API_KEY}',
    'Content-Type': 'application/json'
}
response = requests.post(url, headers=headers, json={'query': query})
data = response.json()  # Parsing the JSON response into a Python dictionary

# Extracting the relevant data
protocols_data = data['data']

# Convert to DataFrame
df = pd.DataFrame(protocols_data)  # Creating a DataFrame from the dictionary

# Connect to SQL database
engine = create_engine('sqlite:///solana_protocols.db')  # Creating a connection to an SQLite database
df.to_sql('protocols', engine, if_exists='replace', index=False)  # Writing the DataFrame to the database table named 'protocols'

print("Data successfully fetched and stored in the database.")



