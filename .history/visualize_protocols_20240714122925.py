import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Function to fetch and visualize data
def visualize_data():
    # Connect to the SQLite database
    engine = create_engine('sqlite:///solana_protocols.db')
    conn = engine.connect()

    # Fetch data from the database
    query = 'SELECT name, revenue FROM protocols ORDER BY revenue DESC'
    df = pd.read_sql_query(query, conn)

    # Close the connection
    conn.close()

    # Plotting the data
    plt.figure(figsize=(14, 8))
    plt.barh(df['name'], df['revenue'], color='skyblue')
    plt.xlabel('Revenue (USD)')
    plt.ylabel('Protocol')
    plt.title('Top 20 Solana Protocols by Revenue')
    plt.gca().invert_yaxis()
    plt.show()

# Main function to call the visualization function
def main():
    visualize_data()

if __name__ == "__main__":
    main()











