import numpy as np
from scipy import linalg

#solve a linear algebra problem:
#x + y = 30
#4x + 9y = 150

testQuestionVariable = np.array([[1,1],[4,9]]) #get the coefficients
testQuestionValue = np.array([30,150]) #get the values

print(linalg.solve(testQuestionVariable, testQuestionValue))