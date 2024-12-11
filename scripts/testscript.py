import pandas as pd
df = pd.read_csv('D:/week 0 data/benin-malanville.csv')
summary_stats = df.describe()
print(summary_stats)