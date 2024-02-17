import pandas as pd

#Create categorical data object
grades = pd.Categorical(['A','A','C', 'F', 'B', 'D', 'B', 'C','F','D'], ordered=True)

print(grades)

#re-order the categorical data object
grades = grades.reorder_categories(['F','D','C','B','A'])

print(grades)