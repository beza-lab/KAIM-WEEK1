import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week1 data/raw_analyst_ratings.csv')

# Extract the domain from the email address
df['domain'] = df['publisher'].apply(lambda x: x.split('@')[1] if '@' in x else x)

# Display the first few rows with the new domain column
print(df.head())

# Count the number of articles per domain
articles_per_domain = df['domain'].value_counts()

# Display the counts
print("Number of articles per domain:")
print(articles_per_domain)
