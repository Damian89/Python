import plotly.express as px
import pandas as pd

# using the tips dataset
df = pd.read_csv('wdmonthname.csv')

# plotting the box chart
fig = px.box(df, x="Month", y="Weight", points='all')

# showing the plot
fig.show()

