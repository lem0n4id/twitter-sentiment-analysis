import streamlit as st
import pandas as pd
import plotly.express as px

# Page title
st.set_page_config(page_title='Sentimental Analysis', page_icon='🤖')
st.title('📈 Sentimental Analysis')

option = st.selectbox(
    'Choose the required stock',
    ('TSLA', 'XYZ'), index=None, placeholder="Select...",)

st.write('You selected:', option)


if option== 'TSLA':

    st.markdown("Tweets of TSLA stock on 30th September 2021")
    TSLA_tweet_sentiments = pd.read_csv("TSLA tweets score.csv")
    TSLA_tweet_sentiments

    TSLA_stock_prices = pd.read_csv("TSLA 14 days stock price.csv")

    st.markdown("Price of TSLA stock")
    fig=px.line(TSLA_stock_prices,x="Date",y="Close")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.markdown("Choose the required stock")