import pandas as pd
import matplotlib.pyplot as plt

# reading the dataset using read_csv
df = pd.read_csv("kcases_week_withDate.csv",
				parse_dates=True,
				index_col="Date")

#plot the data
#df['Weekly Cases'].plot()
df.plot(subplots=True, figsize=(9, 8))

plt.suptitle("Weekly COVID 19 Cases and Deaths, Kalamazoo County")
# show the plot
plt.show()

