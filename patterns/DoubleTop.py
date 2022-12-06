from AlgoTrading import values, high, fig, low
import plotly.graph_objects as go
import numpy as np

# def dist(x, m, c):
#     xint = int(x)
#     if values.iloc[xint].high - m*x - c < 0:
#         return True
#     return False

# def isdown(x1, x2, m, c):
#     if(x2-x1) == 1:
#         return True
#     for i in range(x1+1, x2):
#         if not(dist(high[i], m, c)):
#             return False
#     return True

douTopx = np.array([])
douTopy = np.array([])
i = 1
file = 1
while(i<len(high)-1):
    x1 = int(high[i]) 
    x2 = int(high[i+1])
    y1 = values.iloc[x1].high
    y2 = values.iloc[x2].high
    if(abs(y2 - y1) <20 and x2 - x1 < 30 and x2-x1>8):
        m = (y2-y1)/(x2-x1)
        c = y1 - m*x1
        for x1low in range(x1, x1-35, -1):
            if x1low in low:
                if (values.iloc[x1low].low - y1)/(x1low-x1)>7:
                    for k in range(x1, x2):
                        if(values.iloc[k].low<min(y1, y2)- 50):
                            for x2low in range(x2, x2+35):
                                if x2low in low:
                                    if (values.iloc[x2low].low - y2)/(x2low-x2)<-7:
                                        douTopx = np.append(douTopx, x1low)
                                        douTopx = np.append(douTopx, x1)
                                        douTopx = np.append(douTopx, x2)
                                        douTopx = np.append(douTopx, x2low)
                                        douTopx = np.append(douTopx, None)
                                        douTopx = np.append(douTopx, None)
                                        douTopy = np.append(douTopy, values.iloc[int(x1low)].low)
                                        douTopy = np.append(douTopy, y1)
                                        douTopy = np.append(douTopy, y2)
                                        douTopy = np.append(douTopy, values.iloc[int(x2low)].low)
                                        douTopy = np.append(douTopy, None)
                                        douTopy = np.append(douTopy, None)
                                        str1 = str(values.iloc[x1low:x2])# +","+ str(values.iloc[x1low:x2].close))# + " " + values.iloc[x1low:x2].open + " " + values.iloc[x1low:x2].low)
                                        str2 = str(values.iloc[x2:x2low])# +","+ str(values.iloc[x2:x2low].close))# + " " + values.iloc[x2:x2low].open + " " + values.iloc[x2:x2low].low)
                                        
                                        input = open('ML_data\\input2\\week0\\'+ str(file) +'.txt', 'w')
                                        output = open('ML_data\\target2\\week0\\'+ str(file) +'.txt', 'w')
                                        input.write(str1)
                                        output.write(str2)
                                        input.write('\n')
                                        output.write('\n')
                                        file += 1
                                        input.close()
                                        output.close()
                                        i = i+2
                                        break
                            break
                    break
    i+=1
fig.add_trace(go.Scatter(x=douTopx,y=douTopy, mode="lines",
line=go.scatter.Line(color="black"), showlegend=False))
fig.show()
# for i in range(len(douTopx)):
#     f.write('\n'.join(str(douTopx[i])))
# f.write(str(data))