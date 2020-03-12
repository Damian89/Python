# plotting a single line


# importing the required module 

import matplotlib.pyplot as plt
#import numpy as np
  
# x axis values 
x = [1,2,3,4,5,6,7,8,9,10] 
# corresponding y axis values 
y = [4,8,7,7,7,4,11,9,10,3]
# x tick labels
labels = ['Feb-19','Mar-19','Apr-19','Jun-19','Aug-19','Sep-19','Oct-19','Nov-19','Dec-19','Feb-20'] 
fig = plt.figure()
  
# plotting the graph
plt.plot(x, y) 
plt.scatter(x,y, color = 'black')
plt.xticks(x,labels,rotation=90) # substitutes x tick labels for x numbers

# add regression line
from pylab import polyfit, poly1d
fit = polyfit(x, y, 2)
fit_fn = poly1d(fit)
plt.plot(x, fit_fn(x), color = 'red')

# naming the x axis 
plt.xlabel('Month') 
# naming the y axis 
plt.ylabel('Volunteers')
  
# giving a title to my graph 
plt.title('Volunteers per Month in 2019') 
  
# function to show the plot 
plt.show()
#fig.savefig('lineplot.pdf')
