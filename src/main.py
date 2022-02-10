from trading import *
from test.tradingTest import *

def timeTest(iterations=10):
    totalTime = 0
    computeTime = 0
    stocks = ['FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG']
    for i in range(iterations):
        tempTime = 0
        for stock in stocks:
            tempTime += timeToCompute(ticker=stock)
        computeTime += (tempTime / len(stocks))
        totalTime += tempTime

    computeTime /= iterations
    print("Time To Compute", (iterations * len(stocks)), "Stocks:", totalTime)
    print("---------------------------------")
    print("Average Compute Time", computeTime)

testSimulateBuy()