import pandas as pd
import plotly.graph_objects as go
import numpy as np

global max, min
values = pd.read_csv('data\\banknifty_aug_03.csv')
values.columns = ['time', 'open', 'high' ,'low', 'close', 'Adj close', 'volume']

current = 59
min = 50000
max = 0
for i in range(56, current-2):
    if(values['low'][i]<min):
        min = values['low'][i]
    if(values['high'][i]>max):
        max = values['high'][i]
while(current<len(values)):
    if(values['close'][current-1]>max):
        if(values['high'][current]>values['high'][current-1]):
            print(current, "Buy Call")
            while(values['high'][current]>values['high'][current-1]):
                current+=1
            max = values['high'][current - 1]

    elif(values['close'][current-1]<min):
        if(values['low'][current]<values['low'][current-1]):
            print(current, "Buy Put")
            # current+=1
            while(values['low'][current]<values['low'][current-1]):
                current+=1
            min = values['low'][current - 1]
    current += 1

# fig = go.Figure(data=[go.Candlestick(x=values.index, open = values['open'], 
# high = values['high'], low = values['low'], close = values['close'])])
# fig.update_layout(xaxis_rangeslider_visible=False)
# fig.show()