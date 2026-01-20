import streamlit as st
import yfinance as yf
import pandas as pd
st.title("Stock Price Prediction App")


### yfinance library for yahoo finance data
col1, col2, col3 = st.columns(3)
col1, col2 = st.columns(2)
with col1:  
    #company = st.text_input("Enter Stock Ticker","AAPL")
    company = st.selectbox("Select Stock Ticker",["AAPL","MSFT","GOOGL","AMZN","TSLA"])
with col2:
    sd = st.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
    duration = st.slider("Select the duration (in years) for prediction",1, 10, step= 1)
# with col3:
#     ed = st.date_input("End Date", value=pd.to_datetime("today"))
dat = yf.Ticker(company)
data = pd.DataFrame(dat.history(start = sd, end = sd + pd.DateOffset(years=duration)))
st.write(data.head())
st.subheader("Closing Price Chart over the last year")
st.line_chart(data['Close'])
st.subheader("Volume Chart over the last year")
st.line_chart(data['Volume'])