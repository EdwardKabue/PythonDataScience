import numpy as np

array_1d = np.array([1, 2, 3, 4, 5 ,6])
array_2d = np.array([[1, 2, 3], [4, 5 ,6]])
array_3d = np.array([[[1, 2, 3], [4, 5 ,6]], [[7, 8, 9], [10, 11, 12]]])

#print 1st and 4th elements of array_1d.
print(f"First={array_1d[0]}, Fourth={array_1d[-3]}")

#print 1st and last elements of array_2d.
print(f"First={array_2d[0,0]}, Last={array_2d[1,-1]}")

#print last element of 1st row in array_3d.
print(f"{array_3d[0,1,2]}")

#print last element in array_3d.
print(f"{array_3d[1,1,-1]}")