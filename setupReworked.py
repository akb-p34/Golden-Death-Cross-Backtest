import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas_ta as ta
import numpy as np

startDate = '2017-12-01'
endDate = '2022-12-01'

def chartPrice(ticker, beginning, end):

    # Grabbing data from Yahoo Finance using Pandas Datareader
    adjClose = web.DataReader(ticker, 'yahoo', beginning, end)['Adj Close']

    ma200 = ta.sma(adjClose, 200, talib=True)
    ma50 = ta.sma(adjClose, 50, talib=True)
    
    # Showing final chart
    plt.plot(adjClose)
    plt.plot(ma200)
    plt.plot(ma50)

    intersections = np.argwhere(np.diff(np.sign(ma50 - ma200))).flatten()
    newIntersections = intersections[199:]
    plt.scatter(adjClose.index[newIntersections], ma50[newIntersections], color='purple')

    calculateROI(adjClose, ma200, ma50, newIntersections)

    plotChart(ticker, beginning, end)


stockReturns = []

def calculateROI(price, ma200, ma50, crosses):
    ma50Slope = 0
    ma200Slope = 0
    buySignalIndex = []
    sellSignalIndex = []
    order = []
    ROI = 0.0
    for i in crosses:
        ma50Slope = (ma50[i+1] - ma50[i-1])/2
        ma200Slope = (ma200[i+1] - ma200[i-1])/2
        if (ma50Slope > ma200Slope):
            order.append("Buy")
            buySignalIndex.append(i)
            # Make the intersection green as well
        else:
            order.append("Sell")
            sellSignalIndex.append(i)
            # Make the intersection red as well

    if (order[0]=="Sell"):
        del order[0]
        del sellSignalIndex[0]
    if (order[len(order)-1]=="Buy"):
        del order[len(order)-1]
        del buySignalIndex[len(buySignalIndex)-1]

    for i in range(len(buySignalIndex)):
        ROI += (price[sellSignalIndex[i]]-price[buySignalIndex[i]])/price[buySignalIndex[i]]
    
    stockReturns.append(ROI)

def calculateTotalROI():
    avgReturn = 0.0
    for i in range (len(stockReturns)):
        avgReturn += stockReturns[i]
    avgReturn = avgReturn/len(stockReturns)
    avgReturn = str(round(avgReturn*100)) + '%'
    print("The returns of this portfolio with this trading strategy is " + avgReturn)

def plotChart(ticker, beginning, end):
    # Making additions to chart for presentation
    plt.ylabel('Adjusted Close Price (in $)')
    plt.xlabel('Date')
    plt.xticks(rotation = 45)
    plt.title(ticker + " Adj Close, 50 day SMA, & 200 day SMA from " + beginning + " to " + end)
    plt.legend(["Adj Close", "200D MA", "50D MA"], loc="upper left")
    plt.show()

chartPrice("PFE", startDate, endDate)
chartPrice("AAPL", startDate, endDate)
chartPrice("NKE", startDate, endDate)
chartPrice("F", startDate, endDate)
chartPrice("JPM", startDate, endDate)
chartPrice("CHGG", startDate, endDate)
chartPrice("ETD", startDate, endDate)
chartPrice("CROX", startDate, endDate)
chartPrice("FIVE", startDate, endDate)
chartPrice("FHN", startDate, endDate)

calculateTotalROI()
