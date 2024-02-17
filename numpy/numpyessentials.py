import numpy as np

#zero-dimensional array or Scalars, are the elements in an array. 
#print(np.array(24))

#one-dimensional array
#print(np.array([1,2,3,4]))

#2-dimensional array
#print(np.array([[1,2,3],[4,5,6]]))

#3-dimensional array
numpy_3darr = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]]) 
print( numpy_3darr.shape )
print( numpy_3darr.ndim )