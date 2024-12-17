import pandas as pd
import talib
import matplotlib.pyplot as plt

# Load Tesla historical data into a DataFrame
df = pd.read_csv('D:/week1 data/yfinance_data/TSLA_historical_data.csv')

# Check if the required columns are present 
required_columns = ['Open', 'High', 'Low', 'Close', 'Volume'] 
missing_columns = [col for col in required_columns if col not in df.columns] 
if not missing_columns: print("All required columns are present.") 
else: print(f"Missing columns: {missing_columns}") 

# Calculate Simple Moving Average (SMA)
df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)

# Calculate Exponential Moving Average (EMA)
df['EMA_20'] = talib.EMA(df['Close'], timeperiod=20)

# Calculate Relative Strength Index (RSI)
df['RSI'] = talib.RSI(df['Close'], timeperiod=20)

# Calculate Moving Average Convergence Divergence (MACD)
df['MACD'], df['MACD Signal'], df['MACD Hist'] = talib.MACD(df['Close'])

# Display the DataFrame with the new indicators
print(df.tail())

# Save the DataFrame to a new CSV file with indicators
# df.to_csv('path/to/your/stock_data_with_indicators.csv', index=False)

# Plot the closing prices and a technical indicator of SMA
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['SMA_20'], label='20-day SMA')
plt.title('Stock Price and SMA')
plt.legend()
plt.show()

# Plot the closing prices and a technical indicator of EMA
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['RSI'], label='RSI')
plt.title('Stock Price and RSI')
plt.legend()
plt.show()
