import plotly.express as px
import pandas as pd

# using the tips dataset
df = pd.read_csv('wdmonthname.csv')

# plotting the violin chart
fig = px.violin(df, x="Month", y="Weight", box=True, points='all')
  
# showing the plot
fig.show()
