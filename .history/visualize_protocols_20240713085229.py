import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('solana_protocols.db')

# Replace these with the actual column names
account_column = 'executing_account'
revenue_column = 'total_revenue'

# SQL query to fetch data
query = f"SELECT {account_column}, {revenue_column} FROM protocols"

# Read the data into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Plot the data
plt.figure(figsize=(10, 5))
plt.bar(df[account_column], df[revenue_column])
plt.xlabel('Protocol')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Protocol')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

