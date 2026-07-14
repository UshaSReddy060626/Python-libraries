import pandas as pd
df = pd.DataFrame({
    "Name":["Rahul","Priya","Rahul","Arjun","Sneha"],
    "Maths":[90,None,90,75,85],
    "Science":[85,92,85,80,90],
    "City":["Delhi","Mumbai","Delhi","Chennai","Mumbai"],
    "Passed":["Yes","Yes","Yes","No","Yes"]
})
print(df)
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df = df.drop_duplicates()
df["Total"] = df["Maths"] + df["Science"]
df["Percentage"] = df["Total"] / 2
df["Result"] = df["Passed"].map({"Yes":1,"No":0})
X = df[["Maths","Science","Total","Percentage"]]
print(X)
y = df["Result"]
print(y)
df.to_csv("students_cleaned.csv", index=False)