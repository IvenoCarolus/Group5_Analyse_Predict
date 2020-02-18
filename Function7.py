def stop_words_remover(df):
    """This functions returns a dataframe containing a Without Stop Words column that contains all the words in the tweets that aren't stopwords, takes one dataframe as arg"""
    #Initializing new data frame and result list, which will contain list of words which are not stop words
    new_df = pd.DataFrame([])
    res = []
    counter = 0
    
    #The stop words inside a dictionary
    stop_words_dict = {'stopwords':['where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 
    'thereupon', 'may', 'why', '’s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
    'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 'seeming', 'hence', 'us', 
    'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 'their', 'various', 'thereafter', '‘d', 'above', 'put', 
    'sometime', 'moreover', 'whoever', 'although', 'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 
    'last', 'between', 'still', 'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', '’ve', 'might', 'see', 'whose', 
    'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 'became', 'however', 'many', 
    'thence', 'onto', '‘m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 'becomes', 'alone', 'due', 'being', 'neither', 'a', 
    'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 
    'hereafter', 'whether', 'yet', 'nor', 'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 
    'whenever', 'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 'so', 'both', 
    'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', '’d', 'under', 'while', 'empty', 'doing', 'besides', 'thus', 
    'this', 'anyone', 'its', 'after', 'bottom', 'call', 'n’t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 
    'the', 'all', 'much', 'another', 'since', 'hundred', 'serious', '‘ve', 'ever', 'out', 'full', 'themselves', 'been', 'in', "'d", 
    'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', "'s", "'re", 'most', 'one', "n't", 'into', 'some', 
    'will', 'these', 'twenty', 'here', 'as', 'nobody', 'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', '’ll', 
    'latterly', 'are', 'ten', 'hers', 'should', 'they', '‘s', 'either', 'am', 'be', 'perhaps', '’re', 'only', 'namely', 'sixty', 
    'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 'more', 'sometimes', 
    'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', '‘ll', 'too', 'seems', '’m', 'himself', 'latter', 
    'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', 
    "'ve", 'say', 'via', 'but', 'often', 're', 'our', 'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 
    'eight', 'no', 'hereupon', 'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself',
    'n‘t', 'him', 'could', 'front', 'within', '‘re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 'same', 'were', 
    'it', 'every', 'third', 'together']}
    
    #Looping through every row in the twitter_df and extracting the words which do not match any of the stopwords
    for row in df['Tweets']:
        no_stops = [word for word in row.lower().split() if word not in stop_words_dict['stopwords']]
        res.append(no_stops)
        
    #then after this we remove all the urls
    for row in res:
        no_urls = [word for word in row if word[:4] != 'http' or not (word[:5] != 'https')]
        res[counter] = no_urls
        counter+=1
        
    #Now we build the data frame with all necessary columns and entries, using the res list and some of the actual values from twitter_df
    new_df['Tweets'] = df['Tweets']
    new_df['Date'] = df['Date']
    new_df['Without Stop Words'] = res
    
    return new_df
