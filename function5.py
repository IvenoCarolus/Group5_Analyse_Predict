def number_of_tweets_per_day(df):
    """Function returns data frame containing column for numbre of tweets per day and Date, takes one dataframe as arg"""
   
    df['Date'] = [item[:10] for item in df['Date']]  #extracting the date by removing the timestamp
    df['Tweets'] = [1 for item in df['Tweets']]     #replacing each tweet with the number 1.
    
    return df.groupby('Date').sum() #grouping the tweets according to the date and summing the number of tweets per date
