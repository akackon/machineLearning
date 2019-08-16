import pandas as pd

df = pd.read_csv("HR_comma_sep.csv")

print(type(df))
print (df.shape)
print(df.columns)

print(df.head(5))
print(df.tail(5))
print(df.info())

print(df.describe())

print(df["satisfaction_level"])
df2 = df[["satisfaction_level","salary","sales"]]
print(df2)

print(df.sort_values(["impact","number_project"], ascending = [0,1]))