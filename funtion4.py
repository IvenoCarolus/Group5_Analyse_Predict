def extract_municipality_hashtags(df):
    """Extracts all municipality strings and all the hastags. Creates a new dataframe containing columns with those values as entries. Takes one dataframe as arg"""
    
    #Initializing the new data frame
    new_df = pd.DataFrame([])
    
    #creating the dictionary with all @'s
    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

    #creating a list to hold all the municipality strings and a flag variable to track check if key in row
    mun_list = []
    flag = 0

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

    #Initializing a list that will contain all the extracted hashtags
    final_hash = []

    #for-loop looping through every row and extracting the hastags, appending them to final_hash list
    for row in df['Tweets']:
      final_hash.append([string for string in row.lower().split() if string[0][0] == '#'])
    final_hash = [np.nan if x == [] else x for x in final_hash]
    
    #creating the data frame with all the columns, obviously using the list of municipality strings and the extracted hastags, we get our end product.
    new_df['Tweets'] = df['Tweets']
    new_df['Date'] = df['Date']
    new_df['municipality'] = mun_list
    new_df['hashtags'] = final_hash
    
    return new_df
