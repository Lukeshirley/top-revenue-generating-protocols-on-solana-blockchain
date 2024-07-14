import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def visualize_data():
    conn = sqlite3.connect('solana_protocols.db')
    
    query = """
    SELECT name, dailyRevenue FROM protocols
    ORDER BY dailyRevenue DESC
    """
    
    df = pd.read_sql_query(query, conn)
    
    # Check the dataframe structure
    print(df.head())
    
    plt.figure(figsize=(10, 8))
    plt.bar(df['name'], df['dailyRevenue'])
    plt.xlabel('Protocol')
    plt.ylabel('Daily Revenue')
    plt.title('Top Solana Protocols by Daily Revenue')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    
    conn.close()

def main():
    visualize_data()

if __name__ == "__main__":
    main()














