from trading import *

def timeTest(iterations=10):
    total_time = 0
    time_to_compute = 0
    stocks = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']
    for i in range(iterations):
        temp_time = 0
        for stock in stocks:
            temp_time += calculateTable(ticker=stock)
        time_to_compute += (temp_time / len(stocks))
        total_time += temp_time

    time_to_compute /= iterations
    print("Time To Compute", (iterations * len(stocks)), "Stocks:", total_time)
    print("---------------------------------")
    print("Average Compute Time", time_to_compute)

calculateTable(ticker='AMD', show=True)