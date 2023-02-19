from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

# Using graph_objects
import plotly.graph_objects as go

import pandas as pd
df = pd.read_csv('kzooweather.csv')

fig = go.Figure([go.Scatter(x=df['datetime (UTC)'], y=df['temperature (degC)'], fill='tozeroy')],
                layout=go.Layout(
                title=go.layout.Title(text="Kalamazoo Temperature")
                ))
fig.update_xaxes(title="Date")
fig.update_yaxes(title="Temperature (degC)")
fig.show()
