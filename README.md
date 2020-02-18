## Group5_Analyse_Predict
![Heading](https://www.afriforum.co.za/wp-content/uploads/2019/12/Eskom.jpg)

# Python library containing seven functions that will be used to analyse ESKOM data:

* dictionary_of_metrics <br/>
Returns a dictionary with keys 'mean', 'median', 'std', 'var', 'min', and 'max', corresponding to the mean, median, standard deviation, variance, minimum and maximum of the input list, respectively. <br/>
The standard deviation and variance values are unbiased. <br/>
All values are rounded to 2 decimal places.

* five_num_summary <br/>
Takes in a list of integers and returns a dictionary of the five number summary. <br/>
All values are rounded to 2 decimal places. 

* date_parser <br/>
Takes a list of datetime strings as an input, the string contains the date in 'yyyy-mm-dd' format, as well as the time in hh:mm:ss formamt and returns only the date in 'yyyy-mm-dd' format.

* extract_municipality_hashtags <br/>
Takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.

* number_of_tweets_per_day <br/>
 Calculates the number of tweets that were posted per day.

* word_splitter <br/>
Splits the sentences in a dataframe's column into a list of the separate words. The created lists are placed in a column named 'Split Tweets' in the original dataframe

* stop_words_remover <br/>
Removes english stop words from a tweet.

## Download

Just run the following command - `git clone --recursive https://github.com/IvenoCarolus/Group5_Analyse_Predict.git`
