import yfinance as yf
import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Define the ticker and the time period
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-01-01'

# Fetch the stock data
aapl_data = yf.download(ticker, start=start_date, end=end_date)

# Rename columns for consistency
aapl_data.columns = ['Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']

# Create a DataFrame with dates from the AAPL data
dates = aapl_data.index
text_data = pd.DataFrame(dates, columns=['Date'])

# Generate random headlines
headline_samples = [
    "AAPL hits record high",
    "Concerns over AAPL's future growth",
    "AAPL to unveil new product next month",
    "AAPL reports earnings that exceed forecasts",
    "Market downturn affects AAPL",
    "AAPL invests in renewable energy",
    "New AAPL CEO announced",
    "AAPL faces regulatory scrutiny",
    "AAPL rumored to acquire a tech startup",
    "AAPL's market share grows"
]

# Assign a random headline to each date
text_data['Headline'] = np.random.choice(headline_samples, size=len(text_data))

# Display the first few rows of the updated DataFrame
print(text_data.head())

# Define sentiment analysis function
def calculate_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Apply the sentiment analysis function to the headlines
text_data['Sentiment'] = text_data['Headline'].apply(calculate_sentiment)
print(text_data.head())

# Align sentiment scores with the stock closing prices on the same date
combined_data = text_data.set_index('Date').join(aapl_data['Close'])
print(combined_data.head())

# Calculate daily returns
combined_data['Daily Returns'] = combined_data['Close'].pct_change()
print(combined_data.head())

# Calculate correlation between sentiment and daily stock returns
correlation_returns = combined_data['Sentiment'].corr(combined_data['Daily Returns'])
print("Correlation between sentiment and daily stock returns:", correlation_returns)

# Calculate correlation between sentiment and closing prices
correlation_close = combined_data['Sentiment'].corr(combined_data['Close'])
print("Correlation between sentiment and closing prices:", correlation_close)

# Plotting the sentiment scores over time
plt.figure(figsize=(14, 7))
plt.plot(combined_data.index, combined_data['Sentiment'], label='Sentiment Score', color='b')
plt.xlabel('Date')
plt.ylabel('Sentiment Score')
plt.title('Sentiment Scores Over Time')
plt.legend()
plt.show()

# Plotting the stock closing prices over time
plt.figure(figsize=(14, 7))
plt.plot(combined_data.index, combined_data['Close'], label='Stock Closing Price', color='g')
plt.xlabel('Date')
plt.ylabel('Stock Closing Price')
plt.title('Stock Closing Prices Over Time')
plt.legend()
plt.show()

# Scatter plot for sentiment vs. daily returns
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sentiment', y='Daily Returns', data=combined_data)
plt.xlabel('Sentiment Score')
plt.ylabel('Daily Returns')
plt.title('Sentiment vs. Daily Stock Returns')
plt.show()