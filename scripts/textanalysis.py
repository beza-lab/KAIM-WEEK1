import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Download VADER lexicon
nltk.download('vader_lexicon')

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week1 data/raw_analyst_ratings.csv')

# Initialize VADER sentiment intensity analyzer
sid = SentimentIntensityAnalyzer()

# Define a function to categorize the sentiment
def categorize_sentiment(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis to each headline
df['sentiment_scores'] = df['headline'].apply(lambda x: sid.polarity_scores(x)['compound'])
df['sentiment'] = df['sentiment_scores'].apply(categorize_sentiment)

# Display the first few rows with the sentiment scores and categories
print(df.head())

# Count the number of headlines in each sentiment category
sentiment_distribution = df['sentiment'].value_counts()

# Display the sentiment distribution
print("Sentiment Distribution:")
print(sentiment_distribution)

# Plot the sentiment distribution bar chart 
plt.figure(figsize=(8, 6)) 
sentiment_distribution.plot(kind='bar', color=['green', 'red', 'blue']) 
plt.title('Sentiment Distribution of Headlines') 
plt.xlabel('Sentiment') 
plt.ylabel('Number of Headlines') 
plt.show()
