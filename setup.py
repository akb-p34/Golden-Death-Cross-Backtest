import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Retreiving data from 6/18/2021 because it's 365 days before 12/01/2022 + 200 days for 200 day moving average

# Pfizer: PFE
adjClosePFE = yf.download("PFE", start='2021-06-18', end='2022-12-01')

# Apple: AAPL
adjCloseAAPL = yf.download("AAPL", start='2021-06-18', end='2022-12-01')

# Nike: NKE
adjCloseNKE = yf.download("NKE", start='2021-06-18', end='2022-12-01')

# Ford: F
adjCloseF = yf.download("F", start='2021-06-18', end='2022-12-01')

# JP Morgan Chase Co: JPM
adjCloseJPM = yf.download("JPM", start='2021-06-18', end='2022-12-01')

# Chegg: CHGG
adjCloseCHGG = yf.download("CHGG", start='2021-06-18', end='2022-12-01')

# Ethan Allen: ETD
adjCloseETD = yf.download("ETD", start='2021-06-18', end='2022-12-01')

# Crocs: CROX
adjCloseCROX = yf.download("CROX", start='2021-06-18', end='2022-12-01')

# Five Below: FIVE
adjCloseFIVE = yf.download("FIVE", start='2021-06-18', end='2022-12-01')

