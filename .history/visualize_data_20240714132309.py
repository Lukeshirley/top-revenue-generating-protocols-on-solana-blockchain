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
                     color_continuous_scale=['#14F195', '#9945FF'],
                     title='Top Solana Protocols by Daily Revenue | July 14, 2024')

    fig.update_traces(
        textinfo="label+text+value",
        texttemplate="<b>%{label}</b><br>$%{value:,}",
        textfont_size=25,
        textposition='middle center',
        marker=dict(line=dict(color='#000000', width=0))
        textfont=dict(color='white')
    )

    fig.update_layout(
        title_font_size=50,
        title_font_color='white',
        title_x=0.5,
        title_y=0.935,
        paper_bgcolor='#444444',
        plot_bgcolor='#444444',
        font=dict(size=14, color='white')
    )

    fig.show()
    
    conn.close()

def main():
    visualize_data()

if __name__ == "__main__":
    main()

















