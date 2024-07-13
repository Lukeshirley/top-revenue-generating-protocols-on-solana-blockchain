import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('protocols.db')

# Query to fetch protocol and total_revenue from the database
query = 'SELECT protocol, total_revenue FROM protocols'
df = pd.read_sql_query(query, conn)

# Convert hexadecimal total_revenue to integer
df['total_revenue'] = df['total_revenue'].apply(lambda x: int(x, 16))

# Ensure the protocol values are readable
df['protocol'] = df['protocol'].apply(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

# Close the database connection
conn.close()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(df['protocol'], df['total_revenue'])
plt.xlabel('Protocol')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Protocol')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('protocols_revenue.png')
plt.show()



