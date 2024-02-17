import numpy as np

A = np.array([[[1,2,1],[2,2,3]]]) 
B = np.array([3,4,5])

#add array B to A. The values in B will be added to the values in similar positions of the 1-d arrays in A.
# print(np.add(A,B))

# #subtract A from B. The values in the 1-d array of A will be subtracted from the values in similar positions of B.
# print(np.subtract(B,A))

# #multiply A and B
# print(np.multiply(A,B))

# #divide A by B
# print(np.divide(A,B))

#raise all values of A to a power of 2.
#print(np.power(A,2))

#raise all values of A to a power of value in B.
print(np.power(A,B))

