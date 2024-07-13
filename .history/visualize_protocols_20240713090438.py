import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine('sqlite:///solana_protocols.db')
conn = engine.connect()

# Query the data from the database
query = 'SELECT protocol, total_revenue FROM protocols'
df = pd.read_sql_query(query, conn)

# Ensure each value is a valid hexadecimal string before conversion
df['total_revenue'] = df['total_revenue'].apply(lambda x: x.split('0x')[1] if '0x' in x else x)
df['total_revenue'] = df['total_revenue'].apply(lambda x: int(x, 16))

# Scale down the total revenue to billions for better readability
df['total_revenue'] = df['total_revenue'] / 10**9

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df['protocol'], df['total_revenue'])
plt.xlabel('Protocol')
plt.ylabel('Total Revenue (in billions)')
plt.title('Total Revenue by Protocol')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()








