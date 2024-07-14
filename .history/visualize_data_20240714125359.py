import pandas as pd
import plotly.express as px
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
    
    # Filter out rows where dailyRevenue is zero
    df = df[df['dailyRevenue'] > 0]
    
    # Create treemap
    fig = px.treemap(df, path=['name'], values='dailyRevenue',
                     color='dailyRevenue', hover_data=['dailyRevenue'],
                     color_continuous_scale='RdBu',
                     title='Top Solana Protocols by Daily Revenue')

    fig.show()
    
    conn.close()

def main():
    visualize_data()

if __name__ == "__main__":
    main()















