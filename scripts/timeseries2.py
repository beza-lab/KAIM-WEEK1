import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week1 data/raw_analyst_ratings.csv')

# Convert 'publish_date' to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with missing dates
df = df.dropna(subset=['date'])

# Extract the time of publication
df['publish_time'] = df['date'].dt.time

# Extract the hour of publication
df['publish_hour'] = df['date'].dt.hour

# Count the number of articles published at each hour
hourly_publications = df['publish_hour'].value_counts().sort_index()

# Display the counts
print("Number of articles published per hour:")
print(hourly_publications)

# Plot publishing times
plt.figure(figsize=(14, 7))
hourly_publications.plot(kind='bar')
plt.title('Publication Frequency by Hour of the Day')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Articles')
plt.show()
