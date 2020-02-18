def word_splitter(df):
    """Function returns dataframe with Split Tweets column which contains a list of 'words' in every tweet, string must also be lowercase, one dataframe as arg"""
    
    df['Split Tweets'] = [string.lower().split() for string in df['Tweets']] #simply just splitting tweet string using str.split() and then assigning the entries to Tweets column
    return df
