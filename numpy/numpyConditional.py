import numpy as np

x = np.array([i for i in range(10)])

#get new array based on a condition.
#<print(np.where(x%2==0,"Even", "Odd"))

#conditional list.
condlist = [x<5, x>5]

#choice list
choicelist = [x**2,x**3]

#generate array based on condition list where each condition generates a value based on the corresponding choice list item.
print(np.select(condlist, choicelist, default=x))