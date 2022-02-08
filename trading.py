import alpaca_trade_api as alpaca
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import time

# API Info for fetching data, portfolio, etc. from Alpaca
BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = "PK9Z38HYUIBW0WG2920K"
ALPACA_SECRET_KEY = "gzh6o2R7FaIq5j8h4VGq2uWuvpaWnQTtRjQlKsPj"

api = alpaca.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=BASE_URL, api_version='v2')


def makeDataframe(ticker, range=100):
    # Fetch Stock data from last 100 days
    # You can change the day to be minutes, hours, or seconds
    df = api.get_barset(ticker, 'day', limit = range).df

    # Reformat data (drop multiindex, rename columns, reset index)
    df.columns = df.columns.to_flat_index()
    df.columns = [x[1] for x in df.columns]
    df.reset_index(inplace=True)
    # Add columns to run analysis
    df['change'] = df['close'] - df['open']
    # If you change the value of the rolling mean, it will affect the bollinger bands
    df['rolling_mean'] = df['close'].rolling(int(range) // 20 + 1).mean()
    df['rolling_std'] = df['close'].rolling(int(range) // 20 + 1).std()
    df['upper_band'] = df['rolling_mean'] + 2 * df['rolling_std']
    df['lower_band'] = df['rolling_mean'] - 2 * df['rolling_std']
    return df

def printDataframe(df):
    smdf = df.reset_index().drop(columns = 'index')
    graph = smdf.plot(x = 'time', y = ['close', 'rolling_mean', 'upper_band', 'lower_band'])
    graph.fill_between(x = smdf['time'], y1 = smdf['lower_band'], y2 = smdf['upper_band'], alpha = 0.1, color = 'green')
    graph.set_xlabel("Date")
    graph.set_ylabel("Close Price ($)")
    plt.show()

def calculateTable(ticker, range=100, show=False):
    print(ticker)
    #Start the clock to optimize speed and performance
    start_time = time.time()

    df = makeDataframe(ticker='AMD')

    time_to_compute = time.time() - start_time
    # Display the bollinger band graph and data frame data
    if (show):
        printDataframe(df)
    
    return time_to_compute