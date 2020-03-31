"""
An example of plotting with Pandas.

Taken from http://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot.
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Month':['Feb-19','Mar-19','Apr-19','Jun-19','Aug-19','Sep-19','Oct-19','Nov-19','Dec-19','Feb-20'],
    'Volunteers':[4,8,7,7,7,4,11,9,10,3]})

df.plot(kind='bar',x='Month',y='Volunteers',color='blue',rot=90,legend=False,figsize=(12,6))
plt.title("Volunteers per Month in 2019")
plt.xlabel("Month")
plt.ylabel("Volunteers")
plt.show()
