def word_splitter(df):
    """This function returns dataframe with a 'Split Tweets' column containing a list of 'words' (all lowercase) from each tweet,
    this function accepts one dataframe as an argument"""
    
    df['Split Tweets'] = [string.lower().split() for string in df['Tweets']] #Splitting each tweet string and assigning the entries to the Tweets column
    return df
