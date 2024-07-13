import requests
import pandas as pd
import time
from sqlalchemy import create_engine, String
from config import DUNE_API_KEY

query_id = '3915225'  # Your query ID
url = f'https://api.dune.com/api/v1/query/{query_id}/execute'

def check_query_status(execution_id):
    status_url = f'https://api.dune.com/api/v1/execution/{execution_id}/status'
    headers = {
        'x-dune-api-key': DUNE_API_KEY
    }
    response = requests.get(status_url, headers=headers)
    return response.json()

headers = {
    'x-dune-api-key': DUNE_API_KEY,
    'Content-Type': 'application/json'
}
response = requests.post(url, headers=headers)
execution_id = response.json()['execution_id']

status = check_query_status(execution_id)
while status['state'] != 'QUERY_STATE_COMPLETED':
    if status['state'] == 'QUERY_STATE_FAILED':
        print("Query failed:", status)
        exit(1)
    print("Query state:", status['state'])
    time.sleep(10)
    status = check_query_status(execution_id)

result_url = f'https://api.dune.com/api/v1/execution/{execution_id}/results'
response = requests.get(result_url, headers=headers)
data = response.json()

if 'result' in data:
    rows = data['result']['rows']
    df = pd.DataFrame(rows)
    
    # Separate the hexadecimal values correctly
    df['total_revenue'] = df['data'].apply(lambda x: '0x' + x[2:18])
    
    # Group by executing_account and take the first value of total_revenue
    grouped_df = df.groupby('executing_account').first().reset_index()
    grouped_df = grouped_df.rename(columns={'executing_account': 'protocol', 'total_revenue': 'total_revenue'})

    engine = create_engine('sqlite:///solana_protocols.db')
    grouped_df.to_sql('protocols', engine, if_exists='replace', index=False, dtype={'total_revenue': String})

    print("Data successfully fetched, processed, and stored in the database.")
else:
    print("Failed to fetch data:", data)







