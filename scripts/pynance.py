import pandas_datareader as pdr
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week1 data/yfinance_data/META_historical_data.csv')

# Display the first few rows of the loaded CSV data
print(df.head())

# Define the stock symbols and date range
stocks = ['TSLA']  # If you want data specifically for Tesla
start_date = '2020-01-01'
end_date = '2023-12-31'


# Display the first few rows of the fetched data
print(data.head())

# Optionally, save the fetched data to a CSV file for later use
data.to_csv('tsla_stock_data.csv')

# Display the structure of the fetched data
print(data.info())
