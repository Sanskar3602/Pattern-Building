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

candleid = 200
backCandle = 120
arr1 = np.array([])
arrr2 = np.array([])
for i in range(candleid, candleid - backCandle, -1):
    if i in high:
        arr1 = np.append(arr1, i)
        if len(arr1) == 5:
            break
for i in range(candleid, candleid - backCandle, -1):
    if i in low:
        arr2 = np.append(arr2, i)
        if len(arr2) == 5:
            break

# if slopehigh(arr1[0], arr1[1])

