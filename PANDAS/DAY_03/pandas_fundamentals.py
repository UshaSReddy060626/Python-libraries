#creating series
import pandas as pd
marks=pd.Series([90,100,89,78])
print(marks)

#creating own index
marks=pd.Series([90,100,89],
index=["Saransh","Aarav","Rudra"])
print(marks)

#dataframe
student={
    "Name":["Rahul","Priya","Ankit"],
    "Marks":[90,80,95]
}
df=pd.DataFrame(student)
print(df)
print(df.index)
print(df.columns)
print(df.shape)
print(df.info)
print(df.describe())

#reading csv
df=pd.read_csv("student.csv")
print(df)

#saving csv
df.to_csv("students.csv")
print(df)

#selecting columns
s1={
    "age":[21,56,78],
    "city":["Bengaluru","Bengaluru","Bengaluru"]
}
df=pd.DataFrame(s1)
print(df["age"])
print(df[["age","city"]])

#selecting rows
print(df.iloc[0])
print(df.iloc[1])
print(df[df["age"]==21])

#boolean indexing
marks=pd.Series([90,100,89,78])
df=pd.DataFrame(marks,columns=["marks"])
print(df["marks"]>85)

#conditional filtering
data = {
    "Name": ["Rahul", "Priya", "Ankit", "Neha", "Rahul"],
    "Marks": [90, 75, None, 85, 90],
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Delhi"]
}
df = pd.DataFrame(data)
print(df[df["Marks"]>89])
df[df["City"]=="Delhi"]

#isin
print(df[df["Name"].isin(["Rahul", "Neha"])])

#head
print(df.head())

#tail
print(df.tail(2))

#shape
print(df.shape)

#info
df.info()

#describe
print(df.describe())

#value counts
print(df["City"].value_counts())

#unique
print(df["City"].unique())

#nunique
print(df["City"].nunique())

#data cleaning
print(df.isnull())

#dropna
print(df.dropna())

#fillna
print(df.fillna(9))

#replace
print(df.replace("Delhi", "Bangalore"))

# drop duplicate
print(df.drop_duplicates())

# astype
df["Marks"] = df["Marks"].astype(float)

# sorting
print(df.sort_values(by="Marks"))
print(df.sort_values(by="Marks", ascending=False))

#sortindex
print(df.sort_index())

#excel
data = {
    "Name": ["Rahul", "Priya", "Ankit"],
    "Marks": [90, 75, 88]
}
df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)

#read
new_df = pd.read_excel("students.xlsx")
print(new_df)