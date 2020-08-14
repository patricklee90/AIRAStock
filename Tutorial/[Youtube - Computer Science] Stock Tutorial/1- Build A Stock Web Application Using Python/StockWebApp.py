# Description: This is a stock market dashboard to show some charts and data on some stock

# Import the libraries
import streamlit as st
import pandas as pd
from PIL import Image

# Add a title and an image
st.write("""
# Stock Market Web Application
**Visually** show data on a stock! Date range from Jan 2, 2020 - Aug 4, 2020
""")

image = Image.open("D:/ZLegend/work/Youtube/Stock/Tutorial/[Youtube - Computer Science] Stock Tutorial/1- Build A Stock Web Application Using Python/Misc/AiraStock_background_1.png")
st.image(image, use_column_width=True)

# Create a sidebar header
st.sidebar.header("User Input")

# Create a function to get the user input
def get_input():
    start_date = st.sidebar.text_input("Start Date", "2020-01-02")
    end_date = st.sidebar.text_input("End Date", "2020-08-14")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "AMZN")

    return start_date, end_date, stock_symbol

# Create a function to get the company name
def get_company_name(symbol):
    if symbol == 'AMZN':
        return 'Amazon'
    elif symbol == 'TSLA':
        return 'Tesla'
    elif symbol == "GOOG":
        return 'Alphabet'
    else:
        'None'

# Create a function to get the proper company data and the proper timeframe

def get_data(symbol, start, end):

    # Load the data
    if symbol.upper() == 'AMZN':
        df = pd.read_csv("D:/ZLegend/work/Youtube/Stock/Tutorial/[Youtube - Computer Science] Stock Tutorial/1- Build A Stock Web Application Using Python/Data/AMZN.csv")
    elif symbol.upper() == 'TSLA':
        df = pd.read_csv("D:/ZLegend/work/Youtube/Stock/Tutorial/[Youtube - Computer Science] Stock Tutorial/1- Build A Stock Web Application Using Python/Data/TSLA.csv")
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv("D:/ZLegend/work/Youtube/Stock/Tutorial/[Youtube - Computer Science] Stock Tutorial/1- Build A Stock Web Application Using Python/Data/GOOG.csv")
    else:
        df = pd.DataFrame(columns = ['Date', 'Close','Open', 'Volume', 'Adj Close', 'High', 'Low'])

    # Get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # Set the start and end index rows both to 0
    start_row = 0
    end_row = 0

    # Start the date from the top of the data set and go down to see if the users start date is less than or equal to the date in the data set
    for i in range(0, len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i 
            break

    # Start from the bottom of the data set and go up to see if the users end date is greater than or equal to the date in the data set
    for j in range(0, len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) - 1 - j
            break
    
    # Set the index to be the date
    df = df.set_index(pd.to_datetime(df["Date"].values))

    return df.iloc[start_row:end_row + 1, :]

# Get the users input
start, end, symbol = get_input()
# Get the data
df = get_data(symbol, start, end)
company_name = get_company_name(symbol.upper())

# Display the close price
st.header(company_name + " Close Price \n")
st.line_chart(df['Close'])

# Display the volume
st.header(company_name + " Volume \n")
st.line_chart(df['Volume'])

# Get statistics on the data
st.header("Data Statistic")
st.write(df.describe())

