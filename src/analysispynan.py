import pynance as pn
import matplotlib.pyplot as plt

# Fetch Meta stock data
meta_data = pn.data.get('META', start='2020-01-01', end='2023-01-01')

# Display the first few rows of the data
print(meta_data.head())

# Calculate Simple Moving Average (SMA)
meta_data['SMA_30'] = meta_data['Close'].rolling(window=30).mean()

# Calculate Exponential Moving Average (EMA)
meta_data['EMA_30'] = meta_data['Close'].ewm(span=30, adjust=False).mean()



# Display the DataFrame with the new indicators
print(meta_data.tail())

# Plot the closing prices and a technical indicator of SMA
plt.figure(figsize=(14, 7))
plt.plot(meta_data['Close'], label='Close Price')
plt.plot(meta_data['SMA_30'], label='30-day SMA')
plt.title('Meta Stock Price and 30-day SMA')
plt.legend()
plt.show()

# Plot the closing prices and a technical indicator of EMA
plt.figure(figsize=(14, 7))
plt.plot(meta_data['Close'], label='Close Price')
plt.plot(meta_data['EMA_30'], label='30-day EMA')
plt.title('Meta Stock Price and RSI')
plt.legend()
plt.show()