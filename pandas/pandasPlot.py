import pandas as pd

df = pd.read_csv("survey_results_public.csv")
df.plot()

#plot data from a column
df["Age"].plot()

#plot data from a column with a legend.
df["Age"].plot(legend=True)

#plot data using x and y axis from columns.
df["Age"].plot(x="Respondent", y="Age", legend=True)

#Specify the kind of plot. E.g. scatter
df.plot(x="Respondent", y="Age", kind="scatter", legend=True)

#Set the title of a plot. E.g. Sample Plot.
df.plot(title="Sample Plot", figsize=(15,10))