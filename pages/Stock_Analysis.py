'''

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
import ta
from pages.utils.plotly_figure import plotly_table


# setting page config
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="page_with_curl",
    layout="wide"
)

st.title("Stock Analysis")

col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock Ticker", "TSLA")
with col2:
    start_date = st.date_input("Choose Start Date", datetime.date(today.year-1, today.month, today.day)) # today.year-1 matlab aaj se ek saal picche ka year
with col3:
    end_date = st.date_input("Choose End Date", datetime.date(today.year, today.month, today.day))

st.subheader(ticker)

stock = yf.Ticker(ticker)
st.write(stock.info['longBusinessSummary'])
st.write("**Sector:**", stock.info['sector']) # ** means bold
st.write("**Full Time Employees:**", stock.info['fullTimeEmployees'])
st.write("**Website:**", stock.info['website'])

col1, col2 = st.columns(2)

with col1:
    df = pd.DataFrame(index=['Market Cap', 'Beta', 'EPS', 'PE Ratio'])
    df[''] = [stock.info["marketCap"], stock.info["beta"], stock.info["trailingEps"], stock.info["trailingPE"]]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True) # use_container_width=True matlab jo page ka size hai usme poora graph dikhe

with col2:
    df = pd.DataFrame(index=['Quick Ratio', 'Revenue per share', 'Profit Margins',
                             'Debt to Equity', 'Return on Equity'])
    df[''] = [stock.info["quickRatio"], stock.info["revenuePerShare"], stock.info["profitMargins"], stock.info["debtToEquity"], stock.info["returnOnEquity"]]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True)

# Downloading the stock data
data = yf.download(ticker, start = start_date, end = end_date)

# Showing daily change
col1, col2, col3 = st.columns(3)
daily_change = data['Close'].iloc[-1] - data['Close'].iloc[-2] # Subtracting last close price and second last close price
col1.metric("Daily Change", str(round(data['Close'].iloc[-1],2)), str(round(daily_change, 2))) # string mein pass kiya hai aaj ka jo close price hai vo and kitna change hua hai

# Showing last 10 days data
last_10_df = data.tail(10).sort_index(ascending = False).round(3) # Sorting the index in Descending Order
fig_df = plotly_table(last_10_df)
st.write('##### Historical Data (Last 10 Days)') # Set the title
st.plotly_chart(fig_df, use_container_width=True)
'''

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import datetime
import ta
from pages.utils.plotly_figure import plotly_table, close_chart, candlestick, RSI, Moving_average, MACD

# Setting page config
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="📈",
    layout="wide"
)

st.title("Stock Analysis")

col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock Ticker", "TSLA")
with col2:
    start_date = st.date_input("Choose Start Date", datetime.date(today.year-1, today.month, today.day)) # One year back
with col3:
    end_date = st.date_input("Choose End Date", today)

st.subheader(ticker)

# Fetch stock info
stock = yf.Ticker(ticker)
st.write(stock.info.get('longBusinessSummary', 'No summary available'))
st.write("**Sector:**", stock.info.get('sector', 'N/A')) # ** means bold
st.write("**Full Time Employees:**", stock.info.get('fullTimeEmployees', 'N/A'))
st.write("**Website:**", stock.info.get('website', 'N/A'))

col1, col2 = st.columns(2)

with col1:
    df = pd.DataFrame(index=['Market Cap', 'Beta', 'EPS', 'PE Ratio'])
    df[''] = [
        stock.info.get("marketCap", 'N/A'),
        stock.info.get("beta", 'N/A'),
        stock.info.get("trailingEps", 'N/A'),
        stock.info.get("trailingPE", 'N/A')
    ]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True) # use_container_width=True matlab jo page ka size hai usme poora graph dikhe

with col2:
    df = pd.DataFrame(index=['Quick Ratio', 'Revenue per share', 'Profit Margins', 'Debt to Equity', 'Return on Equity'])
    df[''] = [
        stock.info.get("quickRatio", 'N/A'),
        stock.info.get("revenuePerShare", 'N/A'),
        stock.info.get("profitMargins", 'N/A'),
        stock.info.get("debtToEquity", 'N/A'),
        stock.info.get("returnOnEquity", 'N/A')
    ]
    fig_df = plotly_table(df)
    st.plotly_chart(fig_df, use_container_width=True)

# Downloading stock data
data = yf.download(ticker, start=start_date, end=end_date)

# Flatten MultiIndex if present
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

# Show Daily Change
if len(data) > 1:  # Ensure enough data is available
    col1, col2, col3 = st.columns(3)
    
    last_close = data['Close'].iloc[-1].item()  # Extract scalar value
    prev_close = data['Close'].iloc[-2].item()  # Extract scalar value
    daily_change = last_close - prev_close
    
    col1.metric("Daily Change", round(last_close, 2), round(daily_change, 2))
else:
    st.error("Not enough data available to compute daily change.")

# Show Last 10 Days of Data
if not data.empty:
    last_10_df = data.tail(10).sort_index(ascending=False).round(3)
    fig_df = plotly_table(last_10_df)
    st.write('##### Historical Data (Last 10 Days)')
    st.plotly_chart(fig_df, use_container_width=True)
else:
    st.warning("No historical data available for the selected period.")

# Now we have to create the buttons
col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12 = st.columns([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
num_period = ''
with col1:
    if st.button('5D'):
        num_period = '5d'
with col2:
    if st.button('1M'):
        num_period = '1mo'
with col3:
    if st.button('6M'):
        num_period = '6mo'
with col4:
    if st.button('YTD'):
        num_period = 'ytd'
with col5:
    if st.button('1Y'):
        num_period = '1y'
with col6:
    if st.button('5Y'):
        num_period = '5y'
with col7:
    if st.button('MAX'):
        num_period = 'max'

# Creating a dropdown menu for chart type
col1, col2, col3 = st.columns([1,1,4])
with col1:
    chart_type = st.selectbox('', ('Candle', 'Line'))
with col2: # agar char type 'Candle' selected hai toh hume dropdown mein RSI and MACD dikhana hai
    if chart_type == 'Candle':
        indicators = st.selectbox('', ('RSI', 'MACD'))
    else: # agar char type 'Line' selected hai toh hume dropdown mein RSI, Moving Average and MACD dikhana hai
        indicators = st.selectbox('', ('RSI', 'Moving Average', 'MACD'))

# Create a Chart
ticker_ = yf.Ticker(ticker)
new_df1 = ticker_.history(period = 'max') # data will be filtered on the basis of selected button
data1 = ticker_.history(period = 'max') # default chart will be stored here

if num_period == '': # agar number of period i.e. button selected nhi hai so display the chart based on the default values
    if chart_type == 'Candle' and indicators == 'RSI':
        st.plotly_chart(candlestick(data1, '1y'), use_container_width=True)
        st.plotly_chart(RSI(data1, '1y'), use_container_width=True)
    
    if chart_type == 'Candle' and indicators == 'MACD':
        st.plotly_chart(candlestick(data1, '1y'), use_container_width=True)
        st.plotly_chart(MACD(data1, '1y'), use_container_width=True)
    
    if chart_type == 'Line' and indicators == 'RSI':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width=True)
        st.plotly_chart(RSI(data1, '1y'), use_container_width=True)
    
    if chart_type == 'Line' and indicators == 'Moving Average':
        st.plotly_chart(Moving_average(data1, '1y'), use_container_width=True)

    if chart_type == 'Line' and indicators == 'MACD':
        st.plotly_chart(close_chart(data1, '1y'), use_container_width=True)   
        st.plotly_chart(MACD(data1, '1y'), use_container_width=True)

else: # display the chart based on the button selected by the user
    if chart_type == 'Candle' and indicators == 'RSI':
        st.plotly_chart(candlestick(new_df1, num_period), use_container_width=True)
        st.plotly_chart(RSI(new_df1, num_period), use_container_width=True)
    
    if chart_type == 'Candle' and indicators == 'MACD':
        st.plotly_chart(candlestick(new_df1, num_period), use_container_width=True)
        st.plotly_chart(MACD(new_df1, num_period), use_container_width=True)
    
    if chart_type == 'Line' and indicators == 'RSI':
        st.plotly_chart(close_chart(new_df1, num_period), use_container_width=True)
        st.plotly_chart(RSI(new_df1, num_period), use_container_width=True)
    
    if chart_type == 'Line' and indicators == 'Moving Average':
        st.plotly_chart(Moving_average(new_df1, num_period), use_container_width=True)

    if chart_type == 'Line' and indicators == 'MACD':
        st.plotly_chart(close_chart(new_df1, num_period), use_container_width=True)   
        st.plotly_chart(MACD(new_df1, num_period), use_container_width=True)
