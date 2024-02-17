import pandas as pd

#Series is a one-dimensional ndarray with access labels where you can access the elements using the labels.
#Series use numpy in the background which makes them really fast.

l = [x for x in range(5)]

#create a series
s = pd.Series(l) #by default the series has assigned indexes to the items starting from 0 to number of items-1
# print(s)

#Access items using index.
#print(s[3])

#Manually assign custom indexes.
s = pd.Series(l, index=['a','b','c','d','e']) 
#print(s)

#Access items using custom index.
# print(s['e'])

#Indexes can be duplicated.
s = pd.Series(l, index=['a','b','c','d','d']) 
#print(s['d'])

#Create series from dictionary. The dictionary key automatically become the series indexes.
data = {'a':1,'b':2,'c':3,'d':4}
s = pd.Series(data)
# print(s)

#Specify the items to create series from dictionary using dictionary keys.
s = pd.Series(data, index=['a','b'])
#print(s)

#Specifying non-existent key returns NaN.
s = pd.Series(data, index=['a','b','c','f'])
print(s)