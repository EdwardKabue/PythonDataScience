import pandas as pd

#dtype='string' will enable the application of string functions
text = pd.Series(['A','B','C','D','E','F'], dtype='string')

# print(text.str.lower()) #lower the strings.

# print(text.str.cat(sep=' ')) #Concatenate the strings in a series into one string with specified separator.

