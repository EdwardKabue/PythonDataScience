import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style #used to style the grid

randomNumber = np.random.rand(10)
print(randomNumber)

#select the style of the plot.
style.use("ggplot")
#plot the random numbers.
plt.plot(randomNumber, 'g', label='line one', linewidth=2) #'g' makes the plot line colour green. label is the legend label.

#x axis is the number of random numbers.
plt.xlabel("Range")
#y axis is the actual random number.
plt.ylabel("Numbers")

#Title of the plot.
plt.title("First Plot")

plt.legend() #plot the graph based on set conditions
plt.show() #display the created graph.