# a bar plot

import matplotlib.pyplot as plt
# import numpy as np

y = [4,8,7,7,7,4,11,9,10,3]
x = [1,2,3,4,5,6,7,8,9,10] 
# x tick labels
labels = ['Feb-19','Mar-19','Apr-19','Jun-19','Aug-19','Sep-19','Oct-19','Nov-19','Dec-19','Feb-20']
fig = plt.figure()

# bar plot
plt.bar(x, y)
plt.xticks(x,labels,rotation=90) # substitutes x tick labels for x numbers
plt.title('Volunteers per Month in 2019')
plt.xlabel('Month') 
plt.ylabel('Volunteers') 

# add regression line
from pylab import polyfit, poly1d
fit = polyfit(x, y, 2)
fit_fn = poly1d(fit)
plt.plot(x, fit_fn(x), color = 'red')

# show plot and save figure
plt.show()
fig.savefig('barplot.pdf',bbox_inches='tight')
