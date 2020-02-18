def number_of_tweets_per_day(df):
    """Function returns data frame containing column for numbre of tweets per day and Date, takes one dataframe as arg"""
    
    #extracting date - removing timestamp
    df['Date'] = [item[:10] for item in df['Date']]
    
    #replacing each tweet with 1.
    df['Tweets'] = [1 for item in df['Tweets']]
    
    #then returning the sum
    return df.groupby('Date').sum()
