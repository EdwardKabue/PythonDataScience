#Dataframe is used to re-tabulate data.
import pandas as pd

# df = pd.DataFrame()

# print(type(df)) #prints <class 'pandas.core.frame.DataFrame'>

#create dataframe from csv file.
df = pd.read_csv("survey_results_public.csv")

#print(df)

#read first 5 rows of dataframe.
# print(df.head())

# #read last 5 rows of dataframe.
# print(df.tail())

#customise head and tail to print desired number of rows.
# print(df.head(2))
# print(df.tail(3))

#get row based on 0-based indexes.
print(df.iloc[0])

#return a Numpy representation of the DataFrame.
# print(df.values)

#return large file dataframe in chunk sizes. The object returned is an iterable through which we can loop.
# df = pd.read_csv("survey_results_public.csv", chunksize=5)

# for chunk in df:
#     print(chunk)

#filter records returned.
df = df[df["Hobbyist"]=="Yes"]

#print(df)