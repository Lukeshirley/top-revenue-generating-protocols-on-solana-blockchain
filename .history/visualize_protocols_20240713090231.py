import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to SQL database
engine = create_engine('sqlite:///solana_protocols.db')
query = 'SELECT protocol, total_revenue FROM protocols'
df = pd.read_sql_query(query, engine.connect())

# Convert the total_revenue from hexadecimal to decimal
df['total_revenue'] = df['total_revenue'].apply(lambda x: int(x, 16))

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





