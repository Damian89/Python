# import pandas
import pandas as pd

# reading the CSV file
csvFile = pd.read_csv('kcases_week_withDate.csv')

# displaying the contents of the CSV file
print(csvFile)

import plotly.express as px

df_melt = csvFile.melt(
    id_vars='Date',
    value_vars=['Cases', 'Deaths'])

fig = px.line(df_melt, x='Date',y='value',markers=True,facet_col='variable',facet_col_wrap=1,color='variable', width=1000,height=1000, title="COVID-19 Cases and Deaths")
fig.update_yaxes(showticklabels=True, matches=None, title="Number")
fig.show()