import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def visualize_data():
    conn = sqlite3.connect('solana_protocols.db')
    query = "SELECT name, revenue FROM protocols ORDER BY revenue DESC"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Plotting
    plt.figure(figsize=(12, 8))
    plt.bar(df['name'], df['revenue'])
    plt.xlabel('Protocol')
    plt.ylabel('Revenue')
    plt.title('Top 20 Revenue Generating Protocols on Solana')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def main():
    visualize_data()

if __name__ == "__main__":
    main()












