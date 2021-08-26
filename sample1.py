import plotly.graph_objects as go
import pandas as pd
import numpy as np

symbol = 'EEM'
data_df = pd.read_csv('data/EEM.csv')
data_df['Date'] = pd.to_datetime(data_df['Date'])
data_df = data_df.sort_values('Date', ascending=True)
#print(symbol, str(np.min(data_df['Date'])), str(np.max(data_df['Date'])))
data_df = data_df[data_df['Date']> '2019-01-01']

plotly_data = []
layout = []
plotly_data.append(go.Candlestick(x=data_df['Date'],
    open=data_df['Open'],
    high=data_df['High'],
    low=data_df['Low'],
    close=data_df['Close'],
    name=symbol ))

layout = go.Layout(title='iShares MSCI Emerging Markets ETF (EEM)',
    xaxis=dict(title='Date', rangeslider=dict(visible=True)),
    yaxis=dict(title='Price',showgrid=True,color='black',gridwidth=1,gridcolor='LightPink'),
    plot_bgcolor='white',
    paper_bgcolor='lightgray',
    )

fig = go.Figure(data=plotly_data, layout=layout)
fig.show()
