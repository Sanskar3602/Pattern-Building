import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.stats import linregress
from parameters import distance, candleid, backCandle

values = pd.read_csv('data\\banknifty_aug_03.csv')
values.columns = ['time', 'open', 'high' ,'low', 'close', 'Adj close', 'volume']

def impPoints(values, point, left, right):
    high = 1
    low = 1
    for i in range(point-left, point+right+1):
        if point-left<0 or point+right+1>len(values):
            return 0
        elif(values.low[i]<values.low[point]):
            low = 0
        elif(values.high[i]>values.high[point]):
            high =0
    if high:
        return 2
    elif low:
        return 1
    else:
        return 0

values['impPoints'] = values.apply(lambda x: impPoints(values, x.name, distance,
distance), axis = 1)

fig = go.Figure(data=[go.Candlestick(x=values.index, open = values['open'], 
high = values['high'], low = values['low'], close = values['close'])])
# fig.add_scatter(x=values.index, y=values['optimals'], mode="markers",
#                 marker=dict(size=5, color="MediumPurple"),
#                 name="optimals")
fig.update_layout(xaxis_rangeslider_visible=False)

high = np.array([])
low = np.array([])
for i in range(len(values)):
    if values.iloc[i].impPoints == 1:
        low = np.append(low, i)
    elif values.iloc[i].impPoints == 2:
        high = np.append(high, i)

important = np.array([])
for i in range(len(high)):
    for j in range(i+1,len(high)):
        a= int(high[i])
        b= int(high[j])
        if abs(values.iloc[a].high - values.iloc[b].high)<=25 and b-a>5 and b-a<100:
            important = np.append(important, values.iloc[a].high)
            break

for i in range(len(low)):
    for j in range(i+1,len(low)):
        a= int(low[i])
        b= int(low[j])
        if abs(values.iloc[a].low - values.iloc[b].low)<=25 and b-a>5 and b-a<100:
            important = np.append(important, values.iloc[a].low)
            break
important = np.unique(important)
# for i in range(len(important)):
#     fig.add_hline(y=important[i])

# slooope = np.array([])
# backlimit = candleid - backCandle
# i= candleid - 1
# for i in range( candleid - 1, backlimit, -1):
#     # flag1=0
#     if i in high:
#         for j in range(i, backlimit, -1):
#             if j in high and j!=i:
#                 b = values.iloc[i].high
#                 d = values.iloc[j].high
#                 slope = (d-b)/(j-i)
#                 # flag = 0
#                 e = b + slope*(candleid - i)
#                 if len(slooope)==0 and slope> -2 and slope<-0.3:
#                     slooope = np.append(slooope, slope)
#                     fig.add_trace(go.Scatter(x=[j, candleid],
#                     y=[d, e], mode="lines",
#                     line=go.scatter.Line(color="blue"), showlegend=False))

#                 for sloope in slooope:
#                     if not(abs(slope-sloope)>0.16):
#                         # i = np.where (slooope = sloope)
#                         # slooope = np.delete(slooope, i)
#                         flag = 1
#                     else:
#                         continue
#                     if slope> -2 and slope<-0.3:
#                         slooope = np.append(slooope, slope)
#                         slooope = np.unique(slooope)
#                         fig.add_trace(go.Scatter(x=[j, candleid],
#                         y=[d, e], mode="lines",
#                         line=go.scatter.Line(color="blue"), showlegend=False))
#                         break
            

# slooope2 = np.array([])
# for i in range( candleid - 1, candleid -backCandle, -1):
#     if i in low:
#         for j in range(i-1, candleid -backCandle, -1):
#             if j in low:
#                 b = values.iloc[i].low
#                 d = values.iloc[j].low
#                 e = (candleid*d - b*candleid + b*j - d*i)/(j - i)
#                 slope = (d-b)/(j-i)
#                 # print(slope)
#                 if len(slooope2)==0 and slope< 1.5 and slope>0.57:
#                     slooope2 = np.append(slooope2, slope)
#                     fig.add_trace(go.Scatter(x=[j, candleid],
#                     y=[d, e], mode="lines",
#                     line=go.scatter.Line(color="black"), showlegend=False))
#                 flag = 0
#                 for sloope in slooope2:
#                     if abs(slope-sloope)>0.6:
#                         flag = 1
#                     else:
#                         continue
#                     if slope< 1.5 and slope>0.57:
#                         slooope2 = np.append(slooope2, slope)
#                         slooope2 = np.unique(slooope2)
                        # fig.add_trace(go.Scatter(x=[j, candleid],
                        # y=[d, e], mode="lines",
                        # line=go.scatter.Line(color="black"), showlegend=False))
#                         break

upperBoundx = np.array([])
upperBoundy = np.array([])
lowerBoundx = np.array([])
lowerBoundy = np.array([])
checking = 0
for i in range(candleid - backCandle, candleid -1):
    if i in high:
        upperBoundx = np.append(upperBoundx, i)
        checking = i
        upperBoundy = np.append(upperBoundy, values.iloc[i].high)
    elif i in low:
        lowerBoundx = np.append(lowerBoundx, i)
        lowerBoundy = np.append(lowerBoundy, values.iloc[i].low) 
slmin, intercmin, rmin, pmin, semin = linregress(lowerBoundx, lowerBoundy)
slmax, intercmax, rmax, pmax, semax = linregress(upperBoundx, upperBoundy)

# fig.add_trace(go.Scatter(x=lowerBoundx, y=slmin*lowerBoundx + intercmin, mode='lines', name='min slope'))
# fig.add_trace(go.Scatter(x=upperBoundx, y=slmax*upperBoundx + intercmax, mode='lines', name='max slope'))
# fig.show()

nextCandle = candleid + 1
while(nextCandle):
    test = (values.iloc[nextCandle].open + values.iloc[nextCandle].close)/2
    if(test> values.iloc[checking].high + (nextCandle - checking)*slmax):
        # print (nextCandle, "up")
        break
    elif (test< values.iloc[checking].low + (nextCandle - checking)*slmin):
        # print(nextCandle, "down")
        break
    nextCandle +=1