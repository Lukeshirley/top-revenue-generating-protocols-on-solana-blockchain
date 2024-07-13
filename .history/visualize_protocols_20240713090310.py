import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to SQL database
engine = create_engine('sqlite:///solana_protocols.db')
query = 'SELECT protocol, total_revenue FROM protocols'
df = pd.read_sql_query(query, engine.connect())

# Split the concatenated string into individual hex values and sum their decimal conversions
def hex_string_to_sum(hex_string):
    hex_values = hex_string.split('0x')[1:]  # Split and remove empty first entry
    return sum(int(f"0x{hex_val}", 16) for hex_val in hex_values)

df['total_revenue'] = df['total_revenue'].apply(hex_string_to_sum)

# Scale the total revenue to billions for better readability
df['total_revenue'] = df['total_revenue'] / 1e9

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['protocol'], df['total_revenue'])
plt.xlabel('Protocol')
plt.ylabel('Total Revenue (in billions)')
plt.title('Total Revenue by Protocol')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the figure to a file
plt.savefig('protocol_revenue_chart.png')

# Display the plot
plt.show()






