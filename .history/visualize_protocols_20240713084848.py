import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('solana_protocols.db')
cursor = conn.cursor()

# Fetch the data from the SQLite database
query = "SELECT executing_account, total_revenue FROM protocols"
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Display the DataFrame to verify the data
print(df.head())

# Check for any data issues
print(df.info())

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(df['executing_account'], df['total_revenue'])
plt.xlabel('Protocol')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Protocol')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot to a file
plt.savefig('total_revenue_by_protocol.png')

# Display the plot
plt.show()
