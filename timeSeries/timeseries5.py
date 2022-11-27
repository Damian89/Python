# Using graph_objects
import plotly.graph_objects as go

import pandas as pd
df = pd.read_csv('kcases_week_withDate.csv')

fig = go.Figure([go.Scatter(x=df['Date'], y=df['Cases'], fill="tozeroy")],
                layout=go.Layout(
                title=go.layout.Title(text="Kalamazoo County COVID-19 Cases")
                ))
fig.update_xaxes(title="Date")
fig.update_yaxes(title="Cases")
fig.show()

fig = go.Figure([go.Scatter(x=df['Date'], y=df['Deaths'], fill="tozeroy")],
                layout=go.Layout(
                title=go.layout.Title(text="Kalamazoo County COVID-19 Deaths")
                ))
fig.update_xaxes(title="Date")
fig.update_yaxes(title="Deaths")
fig.show()

