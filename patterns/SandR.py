import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import numpy as np

file = "BANKNIFTY.csv"
df = pd.read_csv(file)

df.Date = pd.to_datetime(df.Date)
df = df.set_index('Date')

# mpf.plot(df, type='candle', volume=True)

def isSupport(df,i):
  support = df['Low'][i] < df['Low'][i-1]  and df['Low'][i] < df['Low'][i+1] and df['Low'][i+1] < df['Low'][i+2] and df['Low'][i-1] < df['Low'][i-2]
  return support

def isResistance(df,i):
  resistance = df['High'][i] > df['High'][i-1]  and df['High'][i] > df['High'][i+1] and df['High'][i+1] > df['High'][i+2] and df['High'][i-1] > df['High'][i-2]
  return resistance

levels = []
s =  np.mean(df['High'] - df['Low'])
def isFarFromLevel(l):
   return np.sum([abs(l-x) < s  for x in levels]) == 0

for i in range(2,df.shape[0]-2):
  if isSupport(df,i):
    l = df['Low'][i]
    if isFarFromLevel(l):
      levels.append((i,l))
  elif isResistance(df,i):
    l = df['High'][i]
    if isFarFromLevel(l):
      levels.append((i,l))

pointss = []
for level in levels:
    pointss.append(level[1])
# pointss.reverse()

#mpf.plot(df, hlines=dict(hlines=pointss), type='candle', volume=True)
#def isImportant(pointss,x, optimals):
#optimals = np.unique(optimals)

#mpf.plot(df, hlines=dict(hlines=important), type='candle', volume=True)


