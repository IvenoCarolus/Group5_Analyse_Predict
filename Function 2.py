def five_num_summary(items):
""""This function takes in a list of integers and returns a dictionary of the five number summary
     values are rounded to 2 decimal places""""

    mx = np.max(items)                   # maximum value
    q2 = np.median(items)                # median value
    mn = np.min(items)                   # minumum value 
    q1 = np.percentile(items,25)         # first quartile  
    q3 = np.percentile(items,75)         # third quartile  
    
    return  {'max': mx, 'median': q2, 'min': mn, 'q1': q1, 'q3': q3} #return the five number summary in a dictionary 

    

