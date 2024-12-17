Initial Findings on Descriptive Statistics:
1.	Headline Lengths:
o	Basic statistics for headline lengths have been calculated and displayed. This can provide insights into the average, median, and range of headline lengths.
2.	Articles Per Publisher:
o	The number of articles contributed by each publisher has been counted and displayed. This helps identify the most active publishers in the dataset.
3.	Yearly Trends:
o	The publication dates have been converted to datetime, missing dates have been handled, and the data has been grouped by year to display trends in publication frequency over time. Publication of articles is increasing over time. 

Methodology
1.	Data Loading and Preprocessing:
o	The CSV file was loaded into a pandas DataFrame.
2.	Publisher Activity:
o	Articles were counted per publisher using the value_counts() method in pandas to identify the most active publishers.
3.	Publication Trends Analysis:
o	Publication dates were converted to datetime format and grouped by year to visualize trends.
o	Trends were visualized using matplotlib to illustrate the distribution over time.

Initial Findings on Text Analysis (Sentiment analysis & Topic Modeling):
1.	Categorizing Sentiment:
o	A function to categorize sentiment scores as positive, negative or neutral has been defined.
o	Sentiment analysis has been applied to each headline to obtain sentiment scores and categories.
2.	The first few rows with sentiment scores and categories have been displayed.
3.	The sentiment distribution across positive, negative, and neutral categories has been counted and displayed.
4.	Sentiment distribution Summary
Neutral: 52.65%
Positive: 31.39%
Negative: 15.95%
This breakdown reveals that the majority of the headlines are neutral in sentiment, with positive and negative sentiments making up about one-third and one-sixth of the total, respectively.
Methodology
• The VADER sentiment intensity analyzer from the nltk library was used to categorize sentiment scores as positive, negative, or neutral.
• Sentiment distribution was counted and visualized.

Initial Findings on Time Series Analysis:
1.	Monthly Publication Frequency Over Time:
o	The first plot shows the monthly trends in publication frequency, providing a clear visualization of how often news articles are published each month.
2.	Monthly Publication Frequency with Market Events:
o	The second plot highlights the impact of specific market events on publication frequency by adding vertical lines for the dates of these events. By overlaying specific market events on the publication frequency timeline, distinct spikes were observed around the year 2020.
3.	Hourly Publication Trends:
o	The analysis of hourly publication times reveals specific hours when news articles are most frequently published. This information is crucial for understanding peak times of news activity, which can be valuable for traders and automated trading systems.

Methodology
1.	Data Loading and Preprocessing:
o	Loads the dataset into a pandas DataFrame.
o	Converts the date column to datetime and drops rows with missing dates.
o	Sets the date column as the DataFrame index.
2.	Resampling and Aggregation:
o	Resamples the data to get monthly publication counts.
o	Plots the monthly publication frequency over time.
3.	Highlighting Specific Market Events:
o	Adds vertical lines to the plot to indicate specific market events, making it easier to correlate spikes in publication frequency with these events.

Conclusion
The analysis successfully identified variations in monthly publication frequencies and correlated these with significant market events. This insight is valuable for understanding how external events can drive media activity and influence news coverage.
It also provided valuable insights into the distribution of news publications throughout the day, highlighting peak hours of activity. This information can help optimize the timing of news releases and improve the efficiency of automated trading systems by aligning with periods of high news activity.

Initial Findings on Publisher Analysis
1.	Number of Articles per Publisher:
o	The analysis identified the number of articles contributed by each publisher. The results highlighted the most active publishers.
Methodology
1.	Data Loading and Preprocessing:
o	The dataset was loaded into a pandas DataFrame.
o	Articles per publisher were counted using the value_counts() method.
o	The data was grouped by publisher and news type using the groupby() method, and unstacked for a clear visualization of the distribution.
2.	Visualization:
o	A bar plot was created to display the number of articles per publisher.

Challenges Encountered
1.	Date Parsing:
o	Some publication dates were not in a standard format, requiring additional preprocessing steps to handle missing or invalid dates.

This project also focuses on the detailed analysis of a large corpus of financial news data to discover correlations between news sentiment and stock market movements. 
Quantitative analysis using pynance and TaLib
use TA-Lib to calculate various technical indicators
visuaize data using differnt indicators

Load news and stock prices dataset. Compute the percentage change in daily closing prices to represent stock movements, Conduct sentiment analysis on news headlines. Then Use statistical methods to test the correlation between daily news sentiment scores and stock returns.
