import pandas as pd

def get_sentiment_score(df:pd.DataFrame)->pd.DataFrame:
    """
    This function will take a dataframe as input and return the final sentiment score of the tweets.
    """
    total_negative = df['Negative'].sum()
    total_neutral = df['Neutral'].sum()
    total_positive = df['Positive'].sum()

    # Calculate the total number of tweets
    total_tweets = len(df)

    # Calculate the average sentiment score for each category
    avg_negative = total_negative / total_tweets
    avg_neutral = total_neutral / total_tweets
    avg_positive = total_positive / total_tweets
    
    final_score=avg_positive-avg_negative
    
    return final_score