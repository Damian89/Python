import plotly.express as px
import pandas as pd

df = pd.read_csv('kzooweather.csv')

fig = px.line(df, x = "datetime (UTC)", y = "temperature (degC)")
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Temperature (degC)')
fig.show()


