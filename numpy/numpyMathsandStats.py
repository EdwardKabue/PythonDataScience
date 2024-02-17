import numpy as np

arr = np.array([[4,3,2],[10,1,0],[5,8,24]])

#get minimum value in an array.
#print(np.amin(arr))

#get minimum for each vertical axis
# print(np.amin(arr, axis=0))
#get minimum for each horizontal axis
# print(np.amin(arr, axis=1))

#get maximum value in an array.
#print(np.max(arr))

#get maximum for each vertical axis
#print(np.amax(arr, axis=0))
#get maximum for each horizontal axis
#print(np.amax(arr, axis=1))

#get the median value of the array.
# print(np.median(arr))

# get the mean value of the array.
# print(np.mean(arr))

# get the standard deviation of the array.
# print(np.std(arr))

# get the variance of the array.
# print(np.var(arr))

# get percentile value.
# print(np.percentile(arr, 50))

deg = np.array([0,30,45,60,90])

#get sin values. Ensure angles are in radians.
print(np.sin(deg*np.pi/180))

#get cos values. Ensure angles are in radians.
print(np.cos(deg*np.pi/180))

#get tan values. Ensure angles are in radians.
print(np.tan(deg*np.pi/180))

arr = np.array([0.1,0.8,-2,2,-9.87])

#get the floor values 
print(np.floor(arr))

#get the ceiling values
print(np.ceil(arr))