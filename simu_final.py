import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyfolio as pf
import yfinance as yf
import pandas_datareader as web

#  Assets in the portfolio
tickers = ['CSCO','BP','WMT','NVDA','BRK-B','JNJ','JPM','ARE','EQNR','IBM']

# Asset weights
Weights = [0.05, 0.05, 0.17, 0.05, 0.05, 0.21, 0.05, 0.19, 0.06, 0.11]

price_data = web.get_data_yahoo(tickers,
                               start='2016-01-01',
                               end='2019-12-31')

price_data = price_data['Adj Close']
price_data.index = price_data.index.tz_localize('utc')
print(price_data.index)
'''values = price_data.index.values
new_index_values = []
for i in values:
    i = pd.Timestamp(i)
    new_index_values.append(i)


price_data = price_data.reindex(new_index_values)
print(price_data.index.values)'''

return_data = price_data.pct_change()[1:]
return_data.dropna(inplace=True)

weighted_returns = (Weights * return_data)
print(weighted_returns.head())

# axis =1 tells pandas we want to add
portfolio_returns = weighted_returns.sum(axis=1)
print(portfolio_returns)

cumulative_returns = (portfolio_returns + 1).cumprod()
print(cumulative_returns)

pf.create_full_tear_sheet(portfolio_returns)
