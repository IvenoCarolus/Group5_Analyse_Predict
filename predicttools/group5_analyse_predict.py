def dictionary_of_metrics(items):
    """This function calculates the mean, median, variance, standard deviation, minimum and maximum of of list of items.
       Answers are rounded to 2 decimal placess"""

    # The funstion makes use of the numpy package to generate a five number summary
    return {'mean':round(np.mean(items),2),
            'median':np.median(items),
            'var':round(np.var(items,ddof=1),2),
            'std':round(np.std(items,ddof=1),2),
            'min':np.min(items),
            'max':np.max(items)}

def five_num_summary(items):
      """This function takes in a list of integers and returns a dictionary of the five number summary
      values are rounded to 2 decimal places"""

      mx = np.max(items)                   # maximum value
      q2 = np.median(items)                # median value
      mn = np.min(items)                   # minimum value
      q1 = np.percentile(items,25)         # first quartile
      q3 = np.percentile(items,75)         # third quartile

      return  {'max': mx, 'median': q2, 'min': mn, 'q1': q1, 'q3': q3} #return the five number summary in a dictionary

def date_parser(date):
    """This function takes a list of datetime strings and converts it into a list of strings with only the date."""

    return [item[:10] for item in date]  #create a new list containing strings of only the first 10 characters of the original strings, i.e the date only.

def extract_municipality_hashtags(df):
    """Extracts all municipality strings and all the hashtags.
    Creates a new dataframe containing columns with those values as entries.
    Takes one dataframe as arg"""

    #creating the dictionary with all @'s
    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

    new_df = pd.DataFrame([])                  #Initializing the new data frame.
    mun_list = []                              #creating a list to hold all the municipality strings.
    final_hash = []                            #creating empty list to hold all the extracted hashtags.
    flag = 0                                   #creating a flag variable to track every key in the row.

    #double for-loop that extracts the municipality strings from every row in the dataframe.
    for row in df['Tweets']:
        flag = 0
        for key in municipality_dict.keys():
            if key in row:
               mun_list.append(municipality_dict[key])
               flag = 1
            break
        if not flag:
          mun_list.append(np.nan)

    #for-loop looping through every row and extracting the hastags, appending them to final_hash list.
    for row in df['Tweets']:
      final_hash.append([string for string in row.lower().split() if string[0][0] == '#'])
    final_hash = [np.nan if x == [] else x for x in final_hash]

    #creating the data frame with all the columns, using the list of municipality strings and the extracted hastags, we get our end product.
    new_df['Tweets'] = df['Tweets']
    new_df['Date'] = df['Date']
    new_df['municipality'] = mun_list
    new_df['hashtags'] = final_hash

    return new_df

def number_of_tweets_per_day(df):
    """Function returns data frame containing column for numbre of tweets per day and Date, takes one dataframe as an argument."""

    df['Date'] = [item[:10] for item in df['Date']]  #extracting the date by slicing up until the first 10 characters in the date string.
    df['Tweets'] = [1 for item in df['Tweets']]     #replacing each tweet with the number 1.

    return df.groupby('Date').sum() #grouping the tweets according to the date and summing the number of tweets per date.

def word_splitter(df):
    """This function returns dataframe with a 'Split Tweets' column containing a list of 'words' (all lowercase) from each tweet,
    this function accepts one dataframe as an argument"""

    df['Split Tweets'] = [string.lower().split() for string in df['Tweets']] #Splitting each tweet string and assigning the entries to the Tweets column
    return df

def stop_words_remover(df):
    """This functions returns a dataframe containing a Without Stop Words column that contains all the words in the tweets that
       aren't stopwords, takes one dataframe as arg"""

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
