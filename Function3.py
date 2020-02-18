def date_pharser(date):     
    """This function takes a list of datetime strings and converts it into a list of strings with only the date."""
    
   #create a new list containing strings of only the first 10 characters of the original strings, i.e the date only.
    return [item[:10] for item in date]  
