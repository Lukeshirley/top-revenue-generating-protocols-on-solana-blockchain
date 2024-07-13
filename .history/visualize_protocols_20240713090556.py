import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine('sqlite:///solana_protocols.db')
conn = engine.connect()

# Query the data
query = 'SELECT protocol, total_revenue FROM protocols'
df = pd.read_sql_query(query, conn)

# Print the dataframe to check the values
print(df)

# Convert the total_revenue column from hexadecimal to integer
df['total_revenue'] = df['total_revenue'].apply(lambda x: int(x, 16))

# Print the dataframe again to check the conversion
print(df)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(df['protocol'], df['total_revenue'])
plt.xlabel('Protocol')
plt.ylabel('Total Revenue (in billions)')
plt.title('Total Revenue by Protocol')
plt.xticks(rotation=45)
plt.show()








