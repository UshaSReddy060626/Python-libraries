import pandas as pd
df = pd.DataFrame({
    "Name":["Amit "," Neha","Karan","Divya"],
    "Marks":[91,84,77,89],
    "City":["Hyderabad","Bangalore","Hyderabad","Pune"],
    "Date":["2026-03-12","2026-04-18","2026-05-25","2026-06-30"],
    "Subject":["Math","Science","Math","Science"]
})
df.to_json("student.json", orient="records", indent=4)
data = pd.read_json("student.json")
print(data)
print(df[df["Marks"].between(80,90)])
print(df.query("Marks > 80"))
df["Name"] = df["Name"].str.strip()
print(df["Name"].str.lower())
print(df["Name"].str.upper())
print(df["Name"].str.contains("a", case=False))
print(df["Name"].str.replace("Amit","Rohan", case=False))
print(df["Name"].str.split())
df["Date"] = pd.to_datetime(df["Date"])
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
print(df[df["Date"] > "2026-04-01"])
city = pd.get_dummies(df["City"])
print(city)
df["Marks"] = df["Marks"] + 5
print(df.memory_usage())
print(df.memory_usage(deep=True))
pivot_df = df.pivot(
    index="Name",
    columns="Subject",
    values="Marks"
)
print(pivot_df)
sales = pd.DataFrame({
    "Student":["Amit","Amit","Neha","Neha"],
    "Subject":["Math","Math","Science","Science"],
    "Marks":[88,92,85,90]
})
pivot_table = sales.pivot_table(
    index="Student",
    columns="Subject",
    values="Marks",
    aggfunc="mean"
)
print(pivot_table)
print(df)