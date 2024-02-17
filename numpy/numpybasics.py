import numpy as np

#numpy array
np_array = np.array([1,2,3,4])
#print(np_array)

#numpy 3x3 array of zeroes.
np_zeroes = np.zeros((3,3))
#print(np_zeroes)

#numpy 3x3 array of ones.
np_ones = np.ones((3,3))
#print(np_ones)

#empty 2x3 numpy array automatically given random numbers
np_empty = np.empty((2,3))
#print(np_empty)

#numpy array with values from a range which is a one-dimensional array.
np_arange = np.arange(12)
#print(np_arange)

#Reshape to make a two-dimensional array.
#print(np_arange.reshape(3,4))
#print(np_arange)

#get equally spaced elements based on start and finish. E.g start at 1, end at 6 and have 5 equally spaced elements.
np_linspace = np.linspace(1,6,5)
#print(np_linspace)

#Three-dimensional array
np_3drange = np.arange(27)
three_d_array = np_3drange.reshape(3,3,3)
print(three_d_array)