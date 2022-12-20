import plotly.express as px
import pandas as pd

df = pd.read_csv('wdmonthname.csv')
fig = px.violin(df, x="Month", y="Weight", box=True, points='all', title="My Weight Each Month, beginning February 2022")  # add point="all" to show all points.
fig.show()
