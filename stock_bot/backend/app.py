from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
from flask_cors import cross_origin
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import datetime as dt
import yfinance as yf
from datetime import datetime
import numpy as np

y_close = None
next_day_op = 0
next_day_cl = 0
y_close_dates = []
y_close_prices = []
y_open_prices = []

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

def prepredict():
    global next_day_op, next_day_cl, y_close_dates, y_close_prices, y_open_prices

    df = yf.download('TSLA', dt.datetime(2010, 1, 1), dt.datetime.now()) # downloading stock data using yahoo finance api from january 1st, 2010 to present day
    df.tail(5) #printing last 5 rows of data

    df = df.drop('Adj Close', axis = 1)

    X_open = df.drop('Open', axis = 1)  
    y_open = df['Open']  

    X_close = df.drop('Close' , axis = 1)
    y_close = df['Close']

    # split the data training and testing sets
    X_train_op, X_test_op, y_train_op, y_test_op = train_test_split(X_open, y_open, test_size = 0.2, random_state = 42)
    X_train_cl, X_test_cl, y_train_cl, y_test_cl = train_test_split(X_close, y_close, test_size = 0.2, random_state = 42)

    # training model using lin reg
    model_op = LinearRegression()
    model_op.fit(X_train_op, y_train_op)

    model_cl = LinearRegression()
    model_cl.fit(X_train_cl, y_train_cl)

    # predicting next day price
    df2 = df
    last_data_op = df.tail(2).drop('Open', axis = 1)
    next_day_op = model_op.predict(last_data_op)

    last_data_cl = df2.tail(1).drop(['Close'], axis=1)
    last_data_cl['Open'] = next_day_op[0]
    next_day_cl = model_cl.predict(last_data_cl)

    y_close_dates = [datetime.strftime(date, "%Y") for date in y_close.index.tolist()]
    y_close_prices = y_close.values.tolist()
    y_open_prices = y_open.values.tolist()

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    # post req 
    data = request.get_json()
    stock_symbol = data['stock_symbol']

    #df operations
    ticker = yf.Ticker(stock_symbol)
    df = yf.download(stock_symbol, dt.datetime(2010, 1, 1), dt.datetime.now())
    ytd_df = yf.download(stock_symbol, dt.datetime(2023, 1, 1), dt.datetime.now())
    df = df.drop('Adj Close', axis = 1)
    X_open = df.drop('Open', axis = 1)  
    y_open = df['Open']  
    X_close = df.drop('Close' , axis = 1)
    y_close = df['Close']
    
    #converting tolist & getting date array
    y_close_dates = [datetime.strftime(date, "%Y") for date in y_close.index.tolist()]
    y_close_prices = y_close.values.tolist()
    y_open_prices = y_open.values.tolist()

    #calculate volatility - ytd (standard deviation * sqrt of ytd days)
    stock_returns = ytd_df['Close'].pct_change()
    volatility = np.std(stock_returns) * np.sqrt(len(ytd_df)) #calculating standard deviation and taking into account the number of trading days per year (ytd)

    #calculate market cap with the formula of outstanding shares * current stock price
    market_cap = ticker.info['marketCap']

    #retrieve volume from df
    volume = ticker.info['volume']

    #retrieve eps from api
    eps = round(ticker.info['trailingEps'], 2)

    #retrieve dividend per yield from api
    dividend_yield = ticker.info['dividendYield']

    #calculate price to earning ratio
    price_earning_ratio = round(ticker.info['currentPrice']/eps, 2)

    #get low and high for today
    low_price = round(ticker.history('1d')['Low'].iloc[-1], 2)
    high_price = round(ticker.history('1d')['High'].iloc[-1], 2)

    # split the data training and testing sets
    X_train_op, X_test_op, y_train_op, y_test_op = train_test_split(X_open, y_open, test_size = 0.2, random_state = 42)
    X_train_cl, X_test_cl, y_train_cl, y_test_cl = train_test_split(X_close, y_close, test_size = 0.2, random_state = 42)

    # training model using lin reg
    model_op = LinearRegression()
    model_op.fit(X_train_op, y_train_op)

    model_cl = LinearRegression()
    model_cl.fit(X_train_cl, y_train_cl)

    test_predictions_op = model_op.predict(X_test_op)
    test_predictions_cl = model_cl.predict(X_test_cl)

    train_predictions_op = model_op.predict(X_train_op)
    train_rmse_op = mean_squared_error(y_train_op, train_predictions_op, squared=False)
    test_predictions_op = model_op.predict(X_test_op)
    test_rmse_op = mean_squared_error(y_test_op, test_predictions_op, squared=False)

    train_predictions_cl = model_cl.predict(X_train_cl)
    train_rmse_cl = mean_squared_error(y_train_cl, train_predictions_cl, squared=False)
    test_predictions_cl = model_cl.predict(X_test_cl)
    test_rmse_cl = mean_squared_error(y_test_cl, test_predictions_cl, squared=False)

    print('Open Test RMSE:', test_rmse_op)
    print('Open Train RMSE:', train_rmse_op)

    print('Close Test RMSE:', test_rmse_cl)
    print('Close Train RMSE:', train_rmse_cl)

    # predicting next day price
    df2 = df
    last_data_op = df.tail(2).drop('Open', axis = 1)
    next_day_price_op = model_op.predict(last_data_op)
    # print(df.tail(2))

    last_data_cl = df2.tail(1).drop(['Close'], axis=1)
    last_data_cl['Open'] = next_day_price_op[0]
    next_day_price_cl = model_cl.predict(last_data_cl)

    return jsonify({
        'next_day_open': round(next_day_price_op[0].item(), 2),
        'next_day_close': round(next_day_price_cl[0].item(), 2),
        'dates': y_close_dates,
        'pricesop': y_open_prices,
        'pricescl': y_close_prices,
        'volatility': volatility,
        'dividend_yield': dividend_yield,
        'market_cap': market_cap,
        'volume': volume,
        'eps': eps,
        'pe_ratio': price_earning_ratio,
        'low': low_price,
        'high': high_price
    })

@app.route('/prepredict', methods=['POST'])
@cross_origin()
def default():
    global next_day_op, next_day_cl, y_close_dates, y_close_prices, y_open_prices
    return jsonify({'next_day_open': round(next_day_op[0], 2), 
                    'next_day_close': round(next_day_cl[0], 2), 
                    'dates': y_close_dates,
                    'pricescl': y_close_prices,
                    'pricesop': y_open_prices
                   })

if __name__ == '__main__':
    prepredict()
    app.run()
