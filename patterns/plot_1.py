import pandas as pd
import mplfinance as mpf

file = "ML_data\\input\\week0\\1.txt"
data = pd.read_csv(file)

# print (data)
# print(data.info())
# print(data.columns)

data.Date = pd.to_datetime(data.Date)
data = data.set_index('Date')

# mpf.plot(data)
mpf.plot(data, type='candle', volume=True)

