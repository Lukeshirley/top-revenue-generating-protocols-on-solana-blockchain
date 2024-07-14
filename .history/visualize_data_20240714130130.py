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
    
    # Define the color scale
    colors = ['#14F195', '#9945FF']
    
    # Create treemap
    fig = px.treemap(df, path=['name'], values='dailyRevenue',
                     color='dailyRevenue', hover_data=['dailyRevenue'],
                     color_continuous_scale=colors)

    # Update the layout for better visualization
    fig.update_traces(texttemplate='%{label}<br>$%{value:,.0f}', textposition='middle center')
    
    fig.update_layout(
        title={
            'text': "Top Solana Protocols by Daily Revenue",
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        title_font=dict(size=20, color='white', family="Arial"),
        margin=dict(t=100, l=25, r=25, b=25),
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)'    # Transparent plot area
    )
    
    fig.show()

    conn.close()

def main():
    visualize_data()

if __name__ == "__main__":
    main()
















