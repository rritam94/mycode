import yfinance as yf

stock = 'TSLA'

def getData(str):
    stock = yf.Ticker(str)
    ticker = yf.Ticker(str).info

    # market_price = ticker['regularMarketPrice']
    previous_close_price = ticker['regularMarketPreviousClose']

    # print('Market Price:', market_price)
    print('Previous Close Price:', previous_close_price)
    
getData(stock)