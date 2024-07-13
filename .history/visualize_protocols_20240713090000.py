import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine('sqlite:///solana_protocols.db')
conn = engine.connect()

# Define the SQL query
query = 'SELECT protocol, total_revenue FROM protocols'

# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query, conn)

# Convert the 'total_revenue' from hex string to decimal
df['total_revenue'] = df['total_revenue'].apply(lambda x: int(x, 16))

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(df['protocol'], df['total_revenue'])
plt.xlabel('Protocol')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Protocol')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the plot
plt.show()



