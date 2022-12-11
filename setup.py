import numpy as np
import pandas_ta as ta
import matplotlib.pyplot as plt
import yfinance as yf

# Tool to help write repetitive code by creating a function to write the stock ticker in Technical Analysis part of code without having to hardcode ticker symbols
tickers = ["PFE", "AAPL", "NKE", "F", "JPM", "CHGG", "ETD", "CROX", "FIVE"]
names = ["Pfizer Inc.", "Apple Inc", "Nike Inc", "Ford Motor Company", "JPMorgan Chase & Co", "Chegg Inc", "Ethan Allen Interiors Inc", "Crocs, Inc.", "Five Below Inc", "First Horizon Corp"]
dates = []
i = -1
j = -1

def currentTicker():
    global i
    i = i + 1
    return tickers[i]

def currentName():
    global j
    j = j + 1
    return names[j]

def getDates(n):
    for i in n:
        dates.append(n[i])

# general function that calculates simple moving avg
def sma(values,window):
    weights = np.repeat(1.0,window)/window
    smas = np.convolve(values,weights,'valid')
    return smas

# Retreiving data from 02/10/2021 - 12/01/2022 because it's 12mo before 12/01/2022 + 200 work days earlier to get 200 day moving average data for the entire back-testing period
startDate = '2021-02-10'
endDate = '2022-12-02'

# Pfizer Inc.: PFE
adjClosePFE = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# General Graph Data
plt.ylabel('Adjusted Close Price (in $)')
plt.xlabel('Date')
plt.xticks(rotation = 45)
plt.title(currentName() + " Adjusted Close Price from " + startDate + " - " + endDate)
plt.legend(loc="upper left")


# Plotting Adjusted Close Price
plt.plot(adjClosePFE, data=adjClosePFE)
# Plotting 200 day Moving avg
#plt.plot(sma(adjClosePFE,200))
# Plotting 50 day Moving avg
#plt.plot(sma(adjClosePFE,50))
plt.show()


#print(type(adjClosePFE.index))
#print(adjClosePFE.index.tolist())
#getDates(adjClosePFE.index)
#print(dates)

# NOTE TO SELF, I WANT TO ADD EACH DATE IF POSSIBLE TO X-AXIS, I ALSO NEED TO PLOT 200 & 50 DAY MOVING AVG & SHADE AREA THAT'S NOT INCLUDED IN ANALYSIS
# ALSO NEED TO ADD CLASSES? ADDITIONAL ITEMS?

'''
# Apple Inc: AAPL
adjCloseAAPL = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# Nike Inc: NKE
adjCloseNKE = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# Ford Motor Company: F
adjCloseF = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# JPMorgan Chase & Co: JPM
adjCloseJPM = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# Chegg Inc: CHGG
adjCloseCHGG = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# Ethan Allen Interiors Inc: ETD
adjCloseETD = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# Crocs, Inc.: CROX
adjCloseCROX = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# Five Below Inc: FIVE
adjCloseFIVE = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

# First Horizon Corp: FHN
adjCloseFHN = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]

'''