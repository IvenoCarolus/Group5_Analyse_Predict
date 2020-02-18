
#Five number summary
def five_num_summary(items):
   
    mx = np.max(items)
    q2 = np.median(items)
    mn = np.min(items)
    q1 = np.percentile(items,25)
    q3 = np.percentile(items,75)
 # Insert the variables within a dictionary.
    dic =  {'max': mx, 'median': q2, 'min': mn, 'q1': q1, 'q3': q3}
#Return the dictionary.
    return dic

