import requests  # Importing the requests library to make HTTP requests
import pandas as pd  # Importing pandas for data manipulation
from sqlalchemy import create_engine  # Importing create_engine from SQLAlchemy to handle SQL database connections

# Example API call (replace with actual API endpoint and parameters)
response = requests.get('https://api.solanabeach.io/v1/protocols')  # Making a GET request to the API endpoint
data = response.json()  # Parsing the JSON response into a Python dictionary

# Print the data to understand its structure
print(data)

# Check if data is a list of dictionaries
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    # Convert to DataFrame
    df = pd.DataFrame(data)  # Creating a DataFrame from the dictionary

    # Connect to SQL database
    engine = create_engine('sqlite:///solana_protocols.db')  # Creating a connection to an SQLite database
    df.to_sql('protocols', engine, if_exists='replace', index=False)  # Writing the DataFrame to the database table named 'protocols'
else:
    print("Data is not in the expected format.")



