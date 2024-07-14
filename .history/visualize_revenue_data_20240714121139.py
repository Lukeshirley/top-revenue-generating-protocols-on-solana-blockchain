import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Load data from SQLite database
engine = create_engine('sqlite:///solana_protocols.db')
df = pd.read_sql('protocols', engine)

# Ensure total_revenue is in billions for better readability
df['fees'] = df['fees'] / 1e9

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(df['name'], df['fees'])
plt.xlabel('Protocol')
plt.ylabel('Total Revenue (in billions)')
plt.title('Total Revenue by Protocol (Top 20 Solana Protocols)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('protocol_revenue_chart.png')
plt.show()
