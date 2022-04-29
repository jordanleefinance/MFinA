import numpy as np
import pandas as pd

stock = np.array([40, 36, 34.2, 20.52, 22.57, 22.34])
index = np.array([150, 150, 145.5, 160.05, 163.25, 159.99])

df = pd.DataFrame(data=[stock, index], index=['AAPL', 'Market'])
df = df.T
df = df.pct_change()
print(df)
cov = df.cov()
var = df['Market'].var()

beta = cov.loc['AAPL', 'Market']/var
print(beta)
