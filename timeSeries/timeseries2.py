# import pandas
import pandas as pd

# reading the CSV file
csvFile = pd.read_csv('kcases_week_withDate.csv')

# displaying the contents of the CSV file
print(csvFile)

import plotly.express as px
figure = px.line(csvFile, x = csvFile.Date, y = "Weekly Cases", title = "COVID 19 Cases, Kalamazoo MI")
figure.show()