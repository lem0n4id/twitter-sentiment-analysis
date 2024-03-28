import streamlit as st
import pandas as pd
import plotly.express as px
import time
from utils import get_sentiment_score
from core import get_tweets, tweets_within_hours, filter_unwanted_tweets
from sentiment_analysis import perform_sentiment_analysis


# Page title
st.set_page_config(page_title='Sentimental Analysis', page_icon='🤖')
st.title('📈 Sentimental Analysis')

option = st.selectbox(
    'Choose the required stock',
    ('TSLA', 'XYZ'), index=None, placeholder="Select...",)

st.write('You selected:', option)


if option== 'TSLA':


    with st.spinner('Wait for it...'):
        time.sleep(3)
    st.success('Done!')

    # tweets table
    st.header("Tweets of TSLA stock on 30th September 2021")

    # df=get_tweets()
    
    # TSLA_tweets_specified=tweets_within_hours(df, datetime='2021-09-30 00:13:26+00:00', stock_name='TSLA', next_x_hours=24)

    # TSLA_tweets_filtered=filter_unwanted_tweets(TSLA_tweets_specified, ticker='TSLA')

    # TSLA_tweets_sentiments=perform_sentiment_analysis(TSLA_tweets_filtered)

    TSLA_tweet_sentiments = pd.read_csv("TSLA tweets score.csv",parse_dates=['Date'], index_col=['Date'])
    TSLA_tweet_sentiments_output=TSLA_tweet_sentiments[['Tweet','Sentiment']]
    st.markdown(f"{len(TSLA_tweet_sentiments_output)} Tweets found")
    TSLA_tweet_sentiments_output

    
    # sentiment
    st.header("Sentiment score of TSLA stock")
    sentiment_score=get_sentiment_score(TSLA_tweet_sentiments)
    st.write(f"The sentiment score of TSLA stock is {round(sentiment_score,2)} on the scale of -1 to 1")

    # add number of positive, negative and neutral tweets

    # box - positive, negative, neutral
    if sentiment_score>0.2:
        st.success("The sentiment score is positive")
    elif sentiment_score<-0.2:
        st.error("The sentiment score is negative")
    else:
        st.warning("The sentiment score is neutral")

    # graph
    st.header("Price of TSLA stock")
    TSLA_stock_prices = pd.read_csv("TSLA 14 days stock price.csv")
    fig=px.line(TSLA_stock_prices,x="Date",y="Close")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.markdown("Choose the required stock")