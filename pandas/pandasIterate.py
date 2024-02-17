import pandas as pd
#Iteration strategies:
#1 Using the index.
#2 Using DataFrame method loc().
#3 Using DataFrame method iloc().
#4 Using DataFrame method iterrows().
#5 Using DataFrame method itertuples().
#6 Using DataFrame method apply().

#Rows of pandas are iterated using index and a for loop.
#If the dataframe has a default index, i.e. starting with 0, then iteration is done using number starting from 0.
#Example:
#create dataframe from csv file.
df = pd.read_csv("survey_results_public.csv")

# iterate through each row and select 'Respondent' and 'MainBranch' columns respectively.
#ind is an intermediate variable indicating the row number.
# for ind in df.index:
#     print(df['Respondent'][ind], df['MainBranch'][ind])

#Iterate using iloc through each row and select # 0th and 2nd index column respectively.
#i is an intermediate variable indicating the row number.
# for i in range(len(df)):
#     print(df.iloc[i, 0], df.iloc[i, 2])

#Iterate using iterrows() through each row and select 'Respondent' and 'MainBranch' columns respectively.
# for index, row in df.iterrows():
#     print(row["Respondent"], row["MainBranch"])

#The apply() method uses a lambda function to simplify the iterating syntax. 
# E.g. iterate through each row and concatenate 'Respondent' and 'Hobbyist' column respectively.
print(df.apply(lambda row: str(row["Respondent"]) + " " + str(row["Hobbyist"]), axis=1))
