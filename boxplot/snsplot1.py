import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('wdmonthname.csv')

sns.stripplot(data=df, x='Month', y='Weight')
sns.boxplot(data=df, x='Month', y='Weight',  notch=True, showfliers=False).set(title='Boxplot of Weight', xlabel='Month', ylabel='Weight (lbs)')

plt.show()

