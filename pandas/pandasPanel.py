import pandas as pd

df = pd.read_csv("survey_results_public.csv")

#set custom indexes.
df.set_index(["Respondent", "Hobbyist"], inplace=True)
#get index
#print(df.index)

#Use loc to get values using custom indexes.
print(df.loc[1])

#Use loc to get values using multiple custom indexes.
print(df.loc[1].loc["Yes"])