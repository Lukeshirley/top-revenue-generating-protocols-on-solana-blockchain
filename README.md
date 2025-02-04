# Top Revenue Generating Protocols on Solana Blockchain

This project fetches, processes, and visualizes data on the top revenue-generating protocols on the Solana blockchain. It uses the DeFi Llama API to fetch the data, stores the data in a SQLite database, and visualizes it using a treemap.

## Features

- **Data Fetching:** Uses the DeFi Llama API to fetch protocol data.
- **Data Processing:** Filters and sorts the data to get the top 20 protocols by daily revenue.
- **Data Storage:** Stores the data in a SQLite database.
- **Data Visualization:** Creates a treemap visualization of the top protocols by daily revenue.

## Prerequisites

- Python 3.7 or higher
- SQLite
- Required Python packages (can be installed via `pip`):
  - pandas
  - plotly
  - requests
  - sqlalchemy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/top-revenue-generating-protocols-on-solana-blockchain.git
    cd top-revenue-generating-protocols-on-solana-blockchain
    ```

2. Set up a virtual environment and activate it:
    ```bash
    python -m venv solana_monitoring_env
    source solana_monitoring_env/bin/activate  # On Windows, use `solana_monitoring_env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Fetch and store data:**
    ```bash
    python fetch_revenue_data.py
    ```

    This script will fetch the latest protocol data from the DeFi Llama API, process it to get the top 20 protocols by daily revenue, and store it in a SQLite database (`solana_protocols.db`).

2. **Visualize the data:**
    ```bash
    python visualize_data.py
    ```

    This script will create a treemap visualization of the top protocols by daily revenue and display it. The visualization includes:
    - Protocol names centered in each rectangle.
    - Daily revenue displayed below the protocol names in accounting format.
    - Colors ranging from Solana Green (#14F195) to Solana Purple (#9945FF).
    - A bold, white title centered above the visualization.
