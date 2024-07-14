import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Function to visualize data
def visualize_data():
    # Connect to the SQLite database
    engine = create_engine('sqlite:///solana_protocols.db')
    conn = engine.connect()

    # Fetch data from the database
    query = 'SELECT protocol, revenue FROM protocols ORDER BY revenue DESC'
    df = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(df['protocol'], df['revenue'])
    plt.xlabel('Protocol')
    plt.ylabel('Revenue (in USD)')
    plt.title('Top 20 Solana Protocols by Revenue')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Main function to call the visualization function
def main():
    visualize_data()

if __name__ == "__main__":
    main()











