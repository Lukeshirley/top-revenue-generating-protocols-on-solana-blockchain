import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('solana_protocols.db')
cursor = conn.cursor()

# Fetch the table schema
cursor.execute("PRAGMA table_info(protocols)")
columns = cursor.fetchall()

# Print the column names
for column in columns:
    print(column)

# Close the database connection
conn.close()
