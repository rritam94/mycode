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
    data = request.get_json()

    stock_symbol = data['stock_symbol']

    df = yf.download(stock_symbol, dt.datetime(2010, 1, 1), dt.datetime.now()) # downloading stock data using yahoo finance api from january 1st, 2010 to present day
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
    print(last_data_cl)

    print('Next day opening stock price:', round(next_day_price_op[0], 2))
    print('Next day closing stock price:', round(next_day_price_cl[0], 20))

    # Should we buy and sell at close tomorrow?
    # buy = False

    # if(next_day_price_op < next_day_price_cl):
    #     print('Buy tomorrow')
    #     buy = True

    # else:
    #     print('Do not buy tomorrow')

    # # Execute this code cell after market closes!!!!

    # curr_data = yf.download("BTC-USD", dt.datetime.now())
    # curr_open = curr_data['Open'][0]
    # curr_close = curr_data['Close'][0]

    # print("Current Day Open: ", curr_open)
    # print("Current Day Close: ", curr_close)

    # if((curr_open < curr_close) == buy):
    #     print('\nYou made money!')

    # elif (curr_open < curr_close and buy == False):
    #     print('\nYou lost the ability to make some money today!')

    # else:
    #     print('\nYou lost money!')

    # y_close_dates = y_close.index.tolist()
    y_close_dates = [datetime.strftime(date, "%Y") for date in y_close.index.tolist()]
    y_close_prices = y_close.values.tolist()
    y_open_prices = y_open.values.tolist()

    print("Previous Closing Price: ", y_close_prices[len(y_close_prices) - 2])

    return jsonify({'next_day_open': round(next_day_price_op[0], 2), 
                    'next_day_close': round(next_day_price_cl[0], 2), 
                    'dates': y_close_dates,
                    'pricescl': y_close_prices,
                    'pricesop': y_open_prices
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
