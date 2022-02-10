from trading import *

# 
# Test that the time is formatted correctly
# 
def testMakeDataFrame():
    df = makeDataframe('AMZN')
    return 0

# Using the data provided test what a stock purchase would have yielded
# The test method buys $500 of the default AAPL stock and will calculate
# the projected profit over a 200 day period
def testSimulateBuy():
    # where it says to buy 
    bank = 100
    holding = 0
    invested = False
    df = makeDataframe('AMZN')
    print(df)
    action_df = df.loc[ df['buy'] != df['sell'] ]
    action_df = action_df.reset_index().drop(columns=['index'])
    action_df = action_df.drop(columns=['open', 'high', 'volume', 'change', 'rolling_mean', 'rolling_std', 'upper_band', 'lower_band'])
    print(action_df)
    for index, row in action_df.iterrows():
        if (row['buy'] & (not invested)):
            holding = bank / row['close']
            bank = 0
            invested = True
            print('Bought ' + str(holding) + ' on ' + str(row['time']))
        elif (row['sell'] & invested):
            bank = holding * row['close']
            holding = 0
            invested = False
    print(df.tail(1)['time'])
    # print('Portfolio Value on', str(df.tail(1)['time']), ' is', str(df.tail(1)['close'] * holding))
    # print(action_df)
    