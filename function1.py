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

