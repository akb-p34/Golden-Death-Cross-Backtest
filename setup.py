import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Tool to help write repetitive code by creating a function to write the stock ticker in Technical Analysis part of code without having to hardcode ticker symbols
tickers = ["PFE", "AAPL", "NKE", "F", "JPM", "CHGG", "ETD", "CROX", "FIVE"]
names = ["Pfizer Inc.", "Apple Inc", "Nike Inc", "Ford Motor Company", "JPMorgan Chase & Co", "Chegg Inc", "Ethan Allen Interiors Inc", "Crocs, Inc.", "Five Below Inc", "First Horizon Corp"]
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

# Retreiving data from 02/10/2021 - 12/01/2022 because it's 12mo before 12/01/2022 + 200 work days earlier to get 200 day moving average data for the entire back-testing period
startDate = '2021-02-10'
endDate = '2022-12-01'

# Pfizer Inc.: PFE
adjClosePFE = yf.download(currentTicker(), start=startDate, end=endDate)["Adj Close"]
plt.plot(adjClosePFE, data=adjClosePFE)
plt.ylabel('Adjusted Close Price (in $)')
plt.xlabel('Date')
plt.xticks(rotation = 90)
plt.title(currentName() + " Adjusted Close Price from " + startDate + " - " + endDate + " (12 mo & 200 days between dates)")
plt.legend(loc="upper left")
plt.show()

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