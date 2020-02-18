def number_of_tweets_per_day(df):
    df['Date'] = [item[:10] for item in df['Date']]
    df['Tweets'] = [1 for item in df['Tweets']]
    
    return df.groupby('Date').sum()
