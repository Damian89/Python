import plotly.express as px
import pandas as pd

df = pd.read_csv('wdmonthname.csv')
fig = px.box(df, x="Month", y="Weight", title="My Weight Each Month, beginning February 2022") # add point="all" to show all points.
fig.show()