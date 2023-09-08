# -*- coding: utf-8 -*-
"""Task_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wsNNjKGLnUaBlTNGGRDIwa-8o3FFmOkm
"""

import yfinance as yf
import numpy as np
import pandas as pd

stocks = pd. read_html('https://en.wikipedia.org/wiki/NIFTY_50') [2].Symbol

stocks.head (5)

stocks = stocks + '.NS'

stocks = stocks.to_list()

df = yf.download(stocks, start= '2012-01-01') ['Close']

df

ret_df = df.pct_change()

ret_df

mtl_ret = (ret_df + 1).resample('M').prod()
mtl_ret

mtl_12 = mtl_ret.rolling(12).apply(np.prod).dropna()

mtl_12

top_ = mtl_12.loc['2012-12-31'].nlargest(5)
top_

top_.name

mtl_ret[top_.name:][1:2]

relevant_ret = mtl_ret[top_.name:][1:2][top_.index]

relevant_ret

relevant_ret.mean(axis=1)

def top_performers(data):
  all_ = mtl_12.loc[data]
  top = all_.nlargest(5)
  relevant_ret = mtl_ret[top.name:][1:2][top.index]
  return (relevant_ret).mean(axis=1).values[0]
top_performers('2012-12-31')

mom_ret = []
for date in mtl_12.index[:-1]:
  mom_ret.append(top_performers(date))

pd.Series(mom_ret)

pd.Series(mom_ret).prod()

nifty = yf.download('^NSEI',start='2012-01-01')['Close']

(nifty.pct_change()+1).prod()