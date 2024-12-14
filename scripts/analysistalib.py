import pandas as pd
import talib
import matplotlib.pyplot as plt

# Load your stock price data into a DataFrame
df = pd.read_csv('D:/week1 data/yfinance_data/META_historical_data.csv')


# Calculate Simple Moving Average (SMA)
df['SMA_20'] = talib.SMA(df['Close'], timeperiod=20)

# Calculate Exponential Moving Average (EMA)
df['EMA_20'] = talib.EMA(df['Close'], timeperiod=20)

# Calculate Relative Strength Index (RSI)
df['RSI'] = talib.RSI(df['Close'], timeperiod=14)

# Calculate Bollinger Bands
# df['Upper Band'], df['Middle Band'], df['Lower Band'] = talib.BBANDS(df['Close'], timeperiod=20)

# Calculate Moving Average Convergence Divergence (MACD)
# df['MACD'], df['MACD Signal'], df['MACD Hist'] = talib.MACD(df['Close'])

# Display the DataFrame with the new indicators
print(df.tail())

# Save the DataFrame to a new CSV file with indicators
# df.to_csv('path/to/your/stock_data_with_indicators.csv', index=False)

# Optional: Plot the closing prices and a technical indicator
plt.figure(figsize=(14, 7))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['SMA_20'], label='20-day SMA')
plt.title('Stock Price and SMA')
plt.legend()
plt.show()
