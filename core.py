import pandas as pd

def get_tweets()->pd.DataFrame:
    """
    This function will read the Stock Tweets for Sentiment Analysis and Prediction dataset and return the dataframe.
    """
    tweets = pd.read_csv("https://raw.githubusercontent.com/lem0n4id/twitter-sentiment-analysis/main/stock_tweets.csv")
    tweets['Date'] = pd.to_datetime(tweets['Date'])
    
    return tweets

def tweets_within_hours(df:pd.DataFrame, datetime:str='2021-09-30 00:13:26+00:00', stock_name:str='TSLA', next_x_hours:int=24) -> pd.DataFrame:
    """
    This function will filter the tweets for the specified stock and within the next x hours from the given datetime.
    """
    # Convert datetime string to datetime object
    datetime = pd.to_datetime(datetime)

    stock_name=stock_name.upper()

    # Filter dataframe for the specified stock and within the next x hours from the given datetime
    filtered_df = df[(df['Stock Name'] == stock_name) &
                     (df['Date'] >= datetime) &
                     (df['Date'] <= datetime + pd.Timedelta(hours=next_x_hours))]

    return filtered_df

def filter_unwanted_tweets(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """
    This function will filter the tweets that contain the specified stock ticker.
    """
    keywords = ['$' + ticker.capitalize(), '$' + ticker.lower(), '$' + ticker.upper(),
                '#' + ticker.capitalize(), '#' + ticker.lower(), '#' + ticker.upper()]

    filtered_tweets = []

    for index, row in df.iterrows():
        tweet = row['Tweet']
        for keyword in keywords:
            if keyword in tweet:
                filtered_tweets.append(row)
                break  # Once a keyword is found, move to the next tweet
                # If you want to include multiple occurrences of the keyword in the same tweet, remove the break statement

    return pd.DataFrame(filtered_tweets)

