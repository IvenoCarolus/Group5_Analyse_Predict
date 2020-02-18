def extract_municipality_hashtags(df):
    new_df = pd.DataFrame([])
    municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

    length = len(df['Tweets'])
    mun_list = []
    flag = 0
    for row in df['Tweets']:
        flag = 0
        for key in municipality_dict.keys():
            if key in row:
               mun_list.append(municipality_dict[key])
               flag = 1
            break
        if not flag:
          mun_list.append(np.nan)

    final_hash = []
    for row in df['Tweets']:
      final_hash.append([string for string in row.lower().split() if string[0][0] == '#'])
    final_hash = [np.nan if x == [] else x for x in final_hash]
    
    new_df['Tweets'] = df['Tweets']
    new_df['Date'] = df['Date']
    new_df['municipality'] = mun_list
    new_df['hashtags'] = final_hash
    
    return new_df