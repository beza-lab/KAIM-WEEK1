import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the news CSV file into a DataFrame
news_df = pd.read_csv('D:/week1 data/raw_analyst_ratings.csv')

# Load META (formerly Facebook) historical stock prices data into a DataFrame
df_meta = pd.read_csv('D:/week1 data/yfinance_data/META_historical_data.csv')

# Check and clean column names
news_df.columns = news_df.columns.str.strip()
df_meta.columns = df_meta.columns.str.strip()

# Print column names to verify
print("News Data Columns:", news_df.columns)
print("META Stock Data Columns:", df_meta.columns)

# Ensure 'date' column is present and convert to datetime format with error handling
if 'date' in news_df.columns:
    news_df['date'] = pd.to_datetime(news_df['date'], format="%Y-%m-%d %H:%M:%S%z", errors='coerce')
else:
    print("The 'date' column is not found in the news DataFrame")

if 'date' in df_meta.columns:
    df_meta['date'] = pd.to_datetime(df_meta['date'], format="%Y-%m-%d %H:%M:%S%z", errors='coerce')
else:
    print("The 'date' column is not found in the META stock DataFrame")

# Drop rows with invalid dates
news_df = news_df.dropna(subset=['date'])
df_meta = df_meta.dropna(subset=['date'])

# Normalize timestamps to just the date
if 'date' in news_df.columns:
    news_df['date'] = news_df['date'].dt.normalize()

if 'date' in df_meta.columns:
    df_meta['date'] = df_meta['date'].dt.normalize()

# Perform sentiment analysis on the news headlines
if 'headline' in news_df.columns:
    news_df['Sentiment'] = news_df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Classify the sentiment as positive, negative, or neutral
    news_df['Sentiment_Label'] = news_df['Sentiment'].apply(lambda x: 'positive' if x > 0 else ('negative' if x < 0 else 'neutral'))

    # Display the DataFrame with sentiment scores and labels
    print(news_df.head())
else:
    print("The 'headline' column is not found in the news DataFrame")

# Merge the news sentiment data with the stock price data based on the date
if 'date' in news_df.columns and 'date' in df_meta.columns:
    merged_df = pd.merge(df_meta, news_df, on='date', how='inner')

    # Ensure merged_df has data
    if merged_df.empty:
        print("Merged DataFrame is empty. Check your data alignment and merging process.")
    else:
        # Calculate the percentage change in stock prices
        merged_df['Price_Change'] = merged_df['Close'].pct_change()

        # Check for missing values
        print("Missing values in merged DataFrame:")
        print(merged_df.isna().sum())

        # Drop rows with missing 'Price_Change' or 'Sentiment'
        merged_df = merged_df.dropna(subset=['Price_Change', 'Sentiment'])

        # Ensure there is valid data for correlation
        if not merged_df.empty:
            # Calculate the correlation between news sentiment and stock price changes
            correlation = merged_df[['Sentiment', 'Price_Change']].corr()

            # Display the correlation
            print("Correlation between News Sentiment and Stock Price Change:")
            print(correlation)

            # Plot sentiment scores over time
            plt.figure(figsize=(14, 7))
            plt.plot(merged_df['date'], merged_df['Sentiment'], label='Sentiment Score', color='b')
            plt.xlabel('Date')
            plt.ylabel('Sentiment Score')
            plt.title('Sentiment Scores Over Time')
            plt.legend()
            plt.show()

            # Plot stock price changes over time
            plt.figure(figsize=(14, 7))
            plt.plot(merged_df['date'], merged_df['Price_Change'], label='Stock Price Change', color='g')
            plt.xlabel('Date')
            plt.ylabel('Percentage Change')
            plt.title('Stock Price Changes Over Time')
            plt.legend()
            plt.show()

            # Scatter plot of sentiment vs stock price change
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x='Sentiment', y='Price_Change', data=merged_df, hue='Sentiment_Label', palette='coolwarm')
            plt.xlabel('Sentiment Score')
            plt.ylabel('Percentage Change in Stock Price')
            plt.title('Correlation between News Sentiment and Stock Price Change')
            plt.legend(title='Sentiment')
            plt.show()
        else:
            print("No valid data for correlation calculation after cleaning.")
else:
    print("Merging failed due to missing 'date' column in one or both DataFrames")
