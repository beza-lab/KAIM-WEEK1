import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week1 data/raw_analyst_ratings.csv')

# Convert 'publish_date' to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Drop rows with missing dates
df = df.dropna(subset=['date'])

# Set the publication date as the index
df.set_index('date', inplace=True)

# Resample the data to get monthly publication counts
monthly_publications = df.resample('ME').size()

# Plot monthly publication trends
plt.figure(figsize=(14, 7))
monthly_publications.plot()
plt.title('Monthly Publication Frequency Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.show()

# Example: Add vertical lines to indicate specific market events
important_dates = ['2019-01-01', '2019-10-01'] 

plt.figure(figsize=(14, 7))
monthly_publications.plot()
for event_date in important_dates:
    plt.axvline(pd.to_datetime(event_date), color='red', linestyle='--', linewidth=1)
plt.title('Monthly Publication Frequency with Market Events')
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.show()