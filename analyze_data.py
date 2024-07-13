from sqlalchemy import create_engine  # Importing create_engine from SQLAlchemy to handle SQL database connections
import pandas as pd  # Importing pandas for data manipulation

engine = create_engine('sqlite:///solana_protocols.db')  # Creating a connection to an SQLite database

query = """
SELECT protocol_name, SUM(revenue) as total_revenue
FROM protocols
GROUP BY protocol_name
ORDER BY total_revenue DESC
LIMIT 10
"""  # SQL query to select protocol names and their total revenues, grouped by protocol name, ordered by total revenue in descending order, limited to top 10 results

top_protocols = pd.read_sql(query, engine)  # Executing the SQL query and storing the result in a DataFrame
print(top_protocols)  # Printing the DataFrame
