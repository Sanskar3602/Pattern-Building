import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv('data.txt')
data.to_csv('data.csv', index = None)
