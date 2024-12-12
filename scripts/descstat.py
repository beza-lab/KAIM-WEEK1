import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week1 data/raw_analyst_ratings.csv')

# Calculate the length of each headline 
df['headline_length'] = df['headline'].apply(len) 

# Display the first few rows with the new length column 
print(df.head())

# Obtain basic statistics for headline lengths 
length_stats = df['headline_length'].describe() 

# Display the statistics 
print("Basic Statistics for Headline Lengths:") 
print(length_stats)

# Count the number of articles per publisher 
articles_per_publisher = df['publisher'].value_counts() 

# Display the counts 
print("Number of articles per publisher:") 
print(articles_per_publisher)

# Convert 'publish_date' to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with missing dates
df = df.dropna(subset=['date'])

# Group by year to see trends in publication frequency
df['year'] = df['date'].dt.year
yearly_trends = df['year'].value_counts().sort_index()

# Plot yearly trends
plt.figure(figsize=(10, 6))
yearly_trends.plot(kind='bar')
plt.title('Publication Frequency by Year')
plt.xlabel('Year')
plt.ylabel('Number of Articles')
plt.show()