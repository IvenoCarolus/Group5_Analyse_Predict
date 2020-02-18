def date_pharser(date):  
   
    #This function takes a list of datetime strings and converts it into a list of strings with only the date.
    
    return  [item[:10] for item in date]
