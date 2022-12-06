import pandas as pd
import numpy as np
import plotly.graph_objects as go


df = pd.read_csv('data\\banknifty_aug_03.csv')
df.columns = ['time', 'open', 'high' ,'low', 'close', 'Adj close', 'volume']

marketprice = 38000
percentage = 0.001

def resistance(df, point):
    flagl = False
    flagr = False
    a = df['high'][point]
    for i in range(1,15):
        b = df['high'][point-i]
        c = df['high'][point+i]
        if point-15<0 or point+15>len(df) or a<b or a<c:
            return 0
        if(flagl or a-b>percentage*marketprice):
            flagl = True
        if(flagr or a-c>percentage*marketprice):
            flagr = True
        if(flagl and flagr):
            return 1
    return 0

print(resistance(df,247))
high = []
highV = []
i=15
while(i<len(df)- 40):
    if(resistance(df, i)):
        val = df['high'][i]
        high.append(i)
        highV.append(val)
        i+=15
    i+=1

fig = go.Figure(data=[go.Candlestick(x=df.index, open = df['open'], 
high = df['high'], low = df['low'], close = df['close'])])
fig.update_layout(xaxis_rangeslider_visible=False)
for i in range(len(highV)):
    fig.add_trace(go.Scatter(x=[high[i], len(df)],
    y=[highV[i], highV[i]], mode="lines", line=go.scatter.Line(color="blue"), showlegend=False))
fig.show()


# while(x<len(df)):

# while(x<len(df)-40):
#     flag = 0
    # highVal = []
    # i=15
    # while(i<x):
    #     if(resistance(i)):
    #         val = df['high'][i]
    #         highVal.append(val)
    #         i+=15
    #     i+=1
    # for k in range(len(highVal)-1):
    #     if(highVal[k]<highVal[k+1]):
    #         highVal.pop(k)
#     print(x, highVal)
#     if(df['high'][x-1]<nextHigh(df['high'][x-1]) and df['high'][x-1]>df['high'][x-2]):
#         if(nextHigh(df['high'][x-1]) < df['high'][x-1]):
#             x+=1
#             continue
#         if(df['high'][x-1]>df['high'][x] and nextHigh(df['high'][x-1]) - df['high'][x-1]<10 and nextHigh(df['high'][x-1]) > df['high'][x-1]):
#             print(x-1)
#             print("put")
#             flag = 1
#             break
#     if flag == 1:
#         break
#     x+=1