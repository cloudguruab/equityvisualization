import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

#time range
start = dt.datetime(2021, 1, 1)
end = dt.datetime.now()

#load data
data = web.DataReader('AAPL', 'yahoo', start=start, end=end)

#Restructure data to match order of import candlestick_ohlc
data = data[['Open', 'High', 'Low', 'Close']]
data.reset_index(inplace=True)

data['Date'] = data['Date'].map(mdates.date2num)
# print(data)

#plotting data
ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_facecolor('black')
ax.set_title('Apple share price', color='white')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, data.values, width=0.5, colorup="g")
plt.show()
