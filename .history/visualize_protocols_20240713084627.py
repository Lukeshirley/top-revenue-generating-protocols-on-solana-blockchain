import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
conn = sqlite3.connect('solana_protocols.db')

# Load the data into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM protocols", conn)

# Close the database connection
conn.close()

# Convert 'total_revenue' to numeric if necessary
df['total_revenue'] = pd.to_numeric(df['total_revenue'], errors='coerce')

# Convert 'date' column to datetime if necessary (uncomment if you have a 'date' column)
# df['date'] = pd.to_datetime(df['date'])

# Display the DataFrame
print(df.head())

# Bar plot of total revenue by protocol
plt.figure(figsize=(12, 8))
sns.barplot(x='protocol', y='total_revenue', data=df)
plt.title('Total Revenue by Protocol')
plt.xlabel('Protocol')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()

# Line plot of total revenue over time by protocol (uncomment if you have a 'date' column)
# plt.figure(figsize=(12, 8))
# sns.lineplot(x='date', y='total_revenue', hue='protocol', data=df)
# plt.title('Revenue Over Time by Protocol')
# plt.xlabel('Date')
# plt.ylabel('Total Revenue')
# plt.xticks(rotation=45)
# plt.legend(title='Protocol')
# plt.show()

# Sum the total revenue by protocol
revenue_by_protocol = df.groupby('protocol')['total_revenue'].sum()

# Pie chart of market share
plt.figure(figsize=(10, 10))
plt.pie(revenue_by_protocol, labels=revenue_by_protocol.index, autopct='%1.1f%%')
plt.title('Market Share by Protocol')
plt.show()
