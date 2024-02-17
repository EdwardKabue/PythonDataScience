import pandas as pd

s = pd.Series([x for x in range(1,11)])

#Access items using 'iloc' method and item index.
# print(s.iloc[5])

#Access items using 'iat' method and item index.
# print(s.iat[0])

#Slice series like list. Negative indices can also be used.
# print(s[5:9])
#print(s[-4:-1])

#get series values based on condition. If condition is false NaN is returned.
#print(s.where(s%2==0))
#specifiy value to return if condition is false.
# print(s.where(s%2==0, 'Odd Number'))
# print(s.where(s%2==0, s**2))

#get series values based on condition and modify the series itself.
s.where(s%2==0, inplace=True)
#print(s)
#drop the NaN values
print(s.dropna())

#replace NaN values with custom value.
print(s.fillna("Filled Value"))