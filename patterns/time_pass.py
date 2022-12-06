from AlgoTrading import values, high, fig, low
import plotly.graph_objects as go
import numpy as np

def slopehigh(x1, x2):
    y1 = values.iloc[int(x1)].high
    y2 = values.iloc[int(x2)].high
    return (y2-y1)/(x2-x1)
def slopelow(x1, x2):
    y1 = values.iloc[int(x1)].low
    y2 = values.iloc[int(x2)].low
    return (y2-y1)/(x2-x1)

ups1 = np.array([])
ups2 = np.array([])
for i in range(len(high)-1, 1, -1):
    c = int(high[i])
    d = int(high[i-1])
    a = values.iloc[c].high
    b = values.iloc[d].high
    m = slopehigh(c, d)
    
    if m<0.1 and m>-0.9:
        ups1 = np.append(ups1,c)
        ups2 = np.append(ups2,a)
        ups1 = np.append(ups1,d)
        ups2 = np.append(ups2,b)
        while(abs(slopehigh(high[i], high[i-1]) - m) <= 0.3):
            d = int(high[i-1])
            b = values.iloc[d].high
            last = len(ups1) -1
            last2 = len(ups2) -1
            ups1 = np.delete(ups1, last)
            ups2 = np.delete(ups2, last2)
            ups1 = np.append(ups1,d)
            ups2 = np.append(ups2,b)
            i-=1
        ups1 = np.append(ups1, None)
        ups1 = np.append(ups1, None)
        ups2 = np.append(ups2, None)
        ups2 = np.append(ups2, None)
    i-=1
fig.add_trace(go.Scatter(x=ups1,y=ups2, mode="lines",
line=go.scatter.Line(color="black"), showlegend=False))

down1 = np.array([])
down2 = np.array([])
for i in range(len(low)-1, 1, -1):
    c = int(low[i])
    d = int(low[i-1])
    a = values.iloc[c].low
    b = values.iloc[d].low
    m = slopelow(c, d)
    
    if m>-0.1 and m<0.9:
        down1 = np.append(down1,c)
        down2 = np.append(down2,a)
        down1 = np.append(down1,d)
        down2 = np.append(down2,b)
        while(abs(slopelow(low[i], low[i-1]) - m) <= 0.3):
            d = int(low[i-1])
            b = values.iloc[d].low
            last = len(down1) -1
            last2 = len(down2) -1
            down1 = np.delete(down1, last)
            down2 = np.delete(down2, last2)
            down1 = np.append(down1,d)
            down2 = np.append(down2,b)
            i-=1
        down1 = np.append(down1, None)
        down1 = np.append(down1, None)
        down2 = np.append(down2, None)
        down2 = np.append(down2, None)
    i-=1
fig.add_trace(go.Scatter(x=down1,y=down2, mode="lines",
line=go.scatter.Line(color="black"), showlegend=False))

fig.show()