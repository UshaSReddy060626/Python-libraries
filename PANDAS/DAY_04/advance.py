#column operations
import pandas as pd
student={
    "name":["aarav","arjun","rudra"],
    "maths":[95,98,99],
    "science":[90,90,90]
}
df=pd.DataFrame(student)
print(df)

#create a new column
df["English"]=[99,99,99]
print(df)

#updating column
df["maths"]=[90,91,92]
print(df)

#update a single value
df.loc[0,"maths"]=100
print(df)

#arithmetic on columns
df["total"]=df["maths"]+df["science"]
print(df)

#map
grade={100:"A+",91:"A",92:"A"}
df["grade"]=df["maths"].map(grade)
print(df)

#apply
df["science"]=df["science"].apply(lambda x:x+5)
print(df)

#lambda
print((lambda x:x*x)(5))
df["square"]=df["maths"].apply(lambda x:x*x)
print(df)

#aggregation
import pandas as pd
df = pd.DataFrame({
    "Name":["Rahul","Priya","Arjun","Swathi","Riya"],
    "Marks":[80,95,70,90,85]
})
print(df)

#sum
print(df["Marks"].sum())

#mean
print(df["Marks"].mean())

#median
print(df["Marks"].median())

#min
print(df["Marks"].min())

#max
print(df["Marks"].max())

#count
print(df["Marks"].count())

#difference
len(df)
print(df.count())

#standard deviation
print(df["Marks"].std())

#variance
print(df["Marks"].var())

#aggregate
print(df["Marks"].agg(["sum","mean","min","max"]))

#group by
df = pd.DataFrame({
 "name":["rahul","priya","arjun","sneha","riya","aman"],
 "class":["a","a","b","b","a","b"],
 "marks":[90,85,75,95,80,88]
})
df.groupby("class")
print(df)

#average
print(df.groupby("class")["marks"].mean())

#sum of marks
print(df.groupby("class")["marks"].sum())

#maximum marks
print(df.groupby("class")["marks"].max())

#minimum marks
print(df.groupby("class")["marks"].min())

#count students
print(df.groupby("class")["marks"].count())

#aggregate
print(
 df.groupby("class")["marks"].agg(["mean","max","min"])
)

#multiple columns
df = pd.DataFrame({
 "name":["rahul","priya","arjun","swathi"],
 "class":["a","a","b","b"],
 "maths":[90,95,75,88],
 "science":[80,91,70,85]
})
print(df.groupby("class").mean(numeric_only=True))

df = pd.DataFrame({
 "name":["rahul","priya","arjun","sneha","riya","aman"],
 "class":["a","a","b","b","a","b"],
 "marks":[90,85,75,95,80,88]
})

#transform
df["class average"] = (
 df.groupby("class")["marks"]
 .transform("mean")
)
print(df)


#merge concat join
students = pd.DataFrame({
    "Roll":[101,102,103],
    "Name":["Rahul","Priya","Arjun"]
})
marks = pd.DataFrame({
    "Roll":[101,102,103],
    "Marks":[90,95,80]
})
df = pd.merge(students, marks, on="Roll")
print(df)

#inner join
students = pd.DataFrame({
    "Roll":[101,102,103],
    "Name":["Rahul","Priya","Arjun"]
})
marks = pd.DataFrame({
    "Roll":[102,103,104],
    "Marks":[95,80,88]
})
print(pd.merge(students, marks, on="Roll", how="inner"))

#left join
print(pd.merge(students, marks,
on="Roll", how="left"))

#right join
print(pd.merge(students, marks,
on="Roll", how="right"))

#outer join 
print(pd.merge(students, marks,
on="Roll",how="outer"))

# vertical concatenation
df1 = pd.DataFrame({"Name": ["Rahul", "Priya"]})
df2 = pd.DataFrame({"Name": ["Arjun", "Sneha"]})
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], ignore_index=True))

#horizontal concatenation
df1 = pd.DataFrame({
    "Name":["Rahul","Priya"]
})
df2 = pd.DataFrame({
    "Marks":[90,95]
})
print(pd.concat([df1,df2], axis=1))

#join
student = pd.DataFrame({
    "Name":["Rahul","Priya"]
}, index=[101,102])
marks = pd.DataFrame({
    "Marks":[90,95]
}, index=[101,102])
print(student.join(marks))

#aiml applications
import pandas as pd

# Create Dataset
df = pd.DataFrame({
    "Name":["Rahul","Priya","Rahul","Arjun","Sneha"],
    "Maths":[90,None,90,75,85],
    "Science":[85,92,85,80,90],
    "City":["Delhi","Mumbai","Delhi","Chennai","Mumbai"],
    "Passed":["Yes","Yes","Yes","No","Yes"]
})

# Display Dataset
print(df)

# First 5 Rows
print(df.head())

# Shape
print(df.shape)

# Columns
print(df.columns)

# Information
print(df.info())

# Missing Values
print(df.isnull().sum())

# Fill Missing Values
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())

# Remove Duplicates
df = df.drop_duplicates()

# Feature Engineering
df["Total"] = df["Maths"] + df["Science"]
df["Percentage"] = df["Total"] / 2

# Label Encoding
df["Result"] = df["Passed"].map({"Yes":1,"No":0})

# Features
X = df[["Maths","Science","Total","Percentage"]]
print(X)

# Labels
y = df["Result"]
print(y)

# Export Dataset
df.to_csv("students_cleaned.csv", index=False)

#create json
df = pd.DataFrame({
    "Name":["Rahul","Priya"],
    "Age":[20,21],
    "City":["Bangalore","Delhi"]
})
df.to_json("students.json", orient="records", indent=4)

#read json
df = pd.read_json("students.json")
print(df)

#between
print(df[df["Age"].between(20,22)])

#&
df[(df["Age"]>=18) & (df["Age"]<=25)]

#query
filtered_df = df.query("20 <= Age <= 22")
print(filtered_df)

#pivot
df = pd.DataFrame({
    "Employee": ["Amit", "Amit", "Neha", "Neha"],
    "Quarter": ["Q1", "Q2", "Q1", "Q2"],
    "Sales": [50000, 60000, 45000, 55000]
})
pivot_df = df.pivot(
    index="Employee",
    columns="Quarter",
    values="Sales"
)
print(pivot_df)

#pivot table
pivot_df = df.pivot_table(
    index="Employee",
    columns="Quarter",
    values="Sales",
    aggfunc="mean"
)
print(pivot_df)

#date handling
df = pd.DataFrame({
    "Employee": ["Amit", "Neha"],
    "Date": ["2026-01-15", "2026-01-20"]
})
df["Date"] = pd.to_datetime(df["Date"])
print(df)
print(df.dtypes)
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df[df["Date"] > "2026-01-01"]
print(df)

#string operations
df = pd.DataFrame({"Name": ["  rahul  "]})
df["Lower"] = df["Name"].str.lower()
df["Upper"] = df["Name"].str.upper()
df["Strip"] = df["Name"].str.strip()
df["Contains"] = df["Name"].str.contains("sharma")
df["Replace"] = df["Name"].str.replace("_", " ")
df["Split"] = df["Name"].str.split("_")
print(df)

#dummies
df = pd.DataFrame({"City": ["Delhi", "Mumbai", "Delhi"]})
df_dummies = pd.get_dummies(df, columns=["City"], dtype=int)
print(df_dummies)

#performance
import numpy as np
df = pd.DataFrame({"Age": np.random.randint(15, 60, size=1_000_000)})
df["Status"] = np.where(df["Age"] >= 18, "Adult", "Minor")
print(df.head())

#memory usage
df1 = pd.DataFrame({"City": ["Delhi"] * 100000})
df1["City"] = df1["City"].astype("category")

#avoid loops
df2 = pd.DataFrame({"Score": [45, 85]})
df2["Result"] = np.where(df2["Score"] >= 50, "Pass", "Fail")
print(df1.dtypes)
print(df2)