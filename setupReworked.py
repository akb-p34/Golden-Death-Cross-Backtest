import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas_ta as ta
import numpy as np

startDate = '2017-12-01'
endDate = '2022-12-01'

def chartPrice(ticker, beginning, end):
    # Grabbing data from Yahoo Finance using Pandas Datareader
    adjClose = web.DataReader(ticker, 'yahoo', beginning, end)['Adj Close']

    # Isolating dates and prices into their own separate lists
    dateList = []
    for i in range (len(adjClose.index)):
        dateList.append(str(adjClose.index[i].date()))

    priceList = []
    for i in range (len(adjClose.index)):
        priceList.append(adjClose[i])

    ma200 = ta.sma(adjClose, 200, talib=True)
    ma50 = ta.sma(adjClose, 50, talib=True)
    
    # Showing final chart
    plt.plot(adjClose)
    plt.plot(ma200)
    plt.plot(ma50)

    ma200Updated = ma200.fillna(0)
    ma50Updated = ma50.fillna(0)

    ma200Values = []
    for i in range (len(ma200Updated.index)):
        ma200Values.append(ma200Updated[i])

    ma50Values = []
    for i in range (len(ma50Updated.index)):
        ma50Values.append(ma50Updated[i])
    

    intersections = np.argwhere(np.diff(np.sign(ma50 - ma200))).flatten()
    plt.scatter(adjClose.index[intersections], ma50[intersections], color='red')
    print(type(intersections))
    print(intersections)

    # Making additions to chart for presentation
    plt.ylabel('Adjusted Close Price (in $)')
    plt.xlabel('Date')
    plt.xticks(rotation = 45)
    plt.title(ticker + " Adj Close, 50 day SMA, & 200 day SMA from " + beginning + " to " + end)
    plt.legend(["Adj Close", "200D MA", "50D MA"], loc="upper left")
    plt.show()

    
    
chartPrice("PFE", startDate, endDate)
#chartPrice("AAPL", startDate, endDate)
