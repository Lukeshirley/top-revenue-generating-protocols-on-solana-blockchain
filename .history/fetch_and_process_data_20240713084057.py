import requests
import pandas as pd
import time  # Import the time module
from sqlalchemy import create_engine
from config import DUNE_API_KEY

# Define the API endpoint for executing a query
query_id = '3915225'  # Your query ID
url = f'https://api.dune.com/api/v1/query/{query_id}/execute'

# Function to check query status
def check_query_status(execution_id):
    status_url = f'https://api.dune.com/api/v1/execution/{execution_id}/status'
    headers = {
        'x-dune-api-key': DUNE_API_KEY
    }
    response = requests.get(status_url, headers=headers)
    return response.json()

# Making a POST request to the Dune Analytics API to execute the query
headers = {
    'x-dune-api-key': DUNE_API_KEY,
    'Content-Type': 'application/json'
}
response = requests.post(url, headers=headers)
execution_id = response.json()['execution_id']

# Check the query status until it is complete
status = check_query_status(execution_id)
while status['state'] != 'QUERY_STATE_COMPLETED':
    if status['state'] == 'QUERY_STATE_FAILED':
        print("Query failed:", status)
        exit(1)
    print("Query state:", status['state'])
    time.sleep(10)  # Wait for 10 seconds before checking again
    status = check_query_status(execution_id)

# Once the query is complete, fetch the results
result_url = f'https://api.dune.com/api/v1/execution/{execution_id}/results'
response = requests.get(result_url, headers=headers)
data = response.json()

# Print the data to understand its structure
print(data)

# Extracting the relevant data
if 'result' in data:
    rows = data['result']['rows']
    df = pd.DataFrame(rows)
    
    # Function to convert hex to decimal
    def hex_to_decimal(hex_str):
        try:
            return int(hex_str, 16)
        except ValueError:
            return 0  # or handle the error as appropriate

    # Apply the conversion function to the 'data' column
    df['total_revenue'] = df['data'].apply(lambda x: hex_to_decimal(x))

    # Group by executing_account and sum the total_revenue
    grouped_df = df.groupby('executing_account')['total_revenue'].sum().reset_index()
    grouped_df = grouped_df.rename(columns={'executing_account': 'protocol', 'total_revenue': 'total_revenue'})

    # Connect to SQL database
    engine = create_engine('sqlite:///solana_protocols.db')
    grouped_df.to_sql('protocols', engine, if_exists='replace', index=False)

    print("Data successfully fetched, processed, and stored in the database.")
else:
    print("Failed to fetch data:", data)


