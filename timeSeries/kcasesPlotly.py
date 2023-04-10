import plotly.express as px
import pandas as pd

df = pd.read_csv('kcasesWithDates.csv')

fig = px.bar(df, x = "Date", y = "Weekly Cases")
fig.show()

# fig = px.bar(df, x = "Date", y = "Weekly Deaths")
# fig.show()
