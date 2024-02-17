import numpy as np

numpy_arr = np.array([x for x in range(1,10)])

#print(numpy_arr)

# print(numpy_arr.reshape(3,3))

# print(numpy_arr)

numpy_arr = np.array([x for x in range(1,13)])
#reshape into 3-d array.
#print(numpy_arr.reshape(2,2,3))
#print(numpy_arr.reshape(3,2,2))

#reshape into different shape if size of data unknown using -1. Last dimension is automatically calculated.
#print(numpy_arr.reshape(2,2,-1))

numpy_arr = numpy_arr.reshape(3,2,2)
#flatten an array
print(numpy_arr.reshape(-1))