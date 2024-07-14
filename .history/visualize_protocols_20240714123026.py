import pandas as pd
from sqlalchemy import create_engine

# Function to inspect the database schema
def inspect_db():
    # Connect to the SQLite database
    engine = create_engine('sqlite:///solana_protocols.db')
    conn = engine.connect()

    # Fetch data from the database
    query = 'SELECT * FROM protocols LIMIT 5'
    df = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    # Display the DataFrame to understand its structure
    print(df.columns)
    print(df.head())

# Main function to call the inspection function
def main():
    inspect_db()

if __name__ == "__main__":
    main()











