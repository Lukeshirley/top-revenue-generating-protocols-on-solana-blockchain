import matplotlib.pyplot as plt  # Importing matplotlib for plotting
import seaborn as sns  # Importing seaborn for statistical data visualization
import pandas as pd  # Importing pandas for data manipulation
from sqlalchemy import create_engine  # Importing create_engine from SQLAlchemy to handle SQL database connections

# Load data
engine = create_engine('sqlite:///solana_protocols.db')  # Creating a connection to an SQLite database
query = """
SELECT protocol_name, SUM(revenue) as total_revenue
FROM protocols
GROUP BY protocol_name
ORDER BY total_revenue DESC
LIMIT 10
"""  # SQL query to select protocol names and their total revenues, grouped by protocol name, ordered by total revenue in descending order, limited to top 10 results
top_protocols = pd.read_sql(query, engine)  # Executing the SQL query and storing the result in a DataFrame

# Bar plot for top protocols by revenue
plt.figure(figsize=(10, 6))  # Setting the figure size for the plot
sns.barplot(data=top_protocols, x='protocol_name', y='total_revenue')  # Creating a bar plot with protocol names on the x-axis and total revenue on the y-axis
plt.xticks(rotation=45)  # Rotating the x-axis labels by 45 degrees for better readability
plt.title('Top Revenue-Generating Protocols on Solana')  # Adding a title to the plot
plt.xlabel('Protocol')  # Adding a label to the x-axis
plt.ylabel('Total Revenue')  # Adding a label to the y-axis
plt.show()  # Displaying the plot
