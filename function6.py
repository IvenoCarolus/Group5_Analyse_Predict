def word_splitter(df):  
    df['Split Tweets'] = [string.lower().split() for string in df['Tweets']]
    return df 
