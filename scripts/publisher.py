import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week1 data/raw_analyst_ratings.csv')

# Count the number of articles per publisher
articles_per_publisher = df['publisher'].value_counts()

# Display the counts
print("Number of articles per publisher:")
print(articles_per_publisher)

# Group by publisher and news type
news_type_by_publisher = df.groupby(['publisher', 'headline']).size().unstack(fill_value=0)

# Display the news type distribution by publisher
print("News type distribution by publisher:")
print(news_type_by_publisher)

# Plot number of articles per publisher
plt.figure(figsize=(12, 8))
articles_per_publisher.plot(kind='bar')
plt.title('Number of Articles per Publisher')
plt.xlabel('Publisher')
plt.ylabel('Number of Articles')
plt.show()

# Plot news type distribution by publisher
news_type_by_publisher.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title('News Type Distribution by Publisher')
plt.xlabel('Publisher')
plt.ylabel('Number of Articles')
plt.show()