import pandas as pd, numpy as np, matplotlib.pyplot as plt
df = pd.read_csv("HR_comma_sep.csv")
print(df.describe())

print(df["satisfaction_level"].describe())
print(df["satisfaction_level"].plot(kind = "box"))

plt.boxplot(df["satisfaction_level"], showmeans = True)
plt.show()

df["satisfaction_level"].plot(kind = "hist")

plt.hist(df["satisfaction_level"], bins = 30)
plt.show()

print(df["satisfaction_level"].var())
print(df["satisfaction_level"].std())
print(df["satisfaction_level"].mean())
print(df["satisfaction_level"].std()/df["satisfaction_level"].mean() * 100)
print(df["satisfaction_level"].skew())
print(df["satisfaction_level"].kurtosis())

plt.show()

print(df["sales"].unique())

print(df["salary"].unique())
pd.crosstab(df["sales"],df["salary"]).plot(kind = "bar", stacked = True)
plt.show()

print(df.columns)

# Numeric and Categorical Variable Exploration
print(df.groupby(["salary"])["satisfaction_level"].mean().plot(kind = "bar"))
plt.show()