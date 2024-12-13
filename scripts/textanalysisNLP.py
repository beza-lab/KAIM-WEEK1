import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')
nltk.download('punkt_tab')

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week1 data/raw_analyst_ratings.csv')

# Define a function to preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return ' '.join(filtered_tokens)

# Apply the preprocessing function to the headlines
df['processed_headline'] = df['headline'].apply(preprocess_text)

# Display the first few rows with the processed text
print(df.head())

# Initialize CountVectorizer to extract top keywords/phrases
vectorizer = CountVectorizer(max_features=20, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['processed_headline'])

# Get the feature names (keywords/phrases)
keywords = vectorizer.get_feature_names_out()

# Sum the occurrences of each keyword/phrase across all documents
keyword_counts = X.toarray().sum(axis=0)

# Create a DataFrame for the keywords and their counts
keyword_df = pd.DataFrame({'keyword': keywords, 'count': keyword_counts})

# Sort the DataFrame by count in descending order
keyword_df = keyword_df.sort_values(by='count', ascending=False)

# Display the top keywords/phrases
print("Top Keywords/Phrases:")
print(keyword_df)