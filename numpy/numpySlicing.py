import numpy as np

array_1d = np.array([1, 2, 3, 4, 5 ,6])
array_2d = np.array([[1, 2, 3], [4, 5 ,6]])
array_3d = np.array([[[1, 2, 3], [4, 5 ,6]], [[7, 8, 9], [10, 11, 12]]])

#slice from index 1 of array_1d
print(f"Slice from index 1 = {array_1d[1:]}")

#slice from index 3 to 5 of array_1d. NB: The result includes the start index, but excludes the end index.
print(f"Slice from index 3 to 5 = {array_1d[3:5]}")

#Slice from index 1 of the second row in array_2d
print(f"{array_2d[1, 1:]}")

#Slice the 2nd array in the first array of array_3d and slice from its 2nd element.
print(f"{array_3d[0, 1:, 1:]}")