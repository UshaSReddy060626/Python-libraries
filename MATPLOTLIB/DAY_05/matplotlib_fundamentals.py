import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y)
plt.show()

#figure
x=[1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y)
plt.show()
plt.figure(figsize=(8,5))

#line color,style,width
plt.plot(x,y,color="red",linestyle="--",linewidth=4)
plt.show()

#marker
x=[1,2,3,4]
y=[10,20,15,25]
plt.plot(x,y)
plt.show()
plt.figure(figsize=(8,5))
plt.plot(x,y,marker="o",markersize=10)
plt.show()

#title
x=["Amit","Neha","Karan","Divya"]
y=[80,90,75,95]
plt.plot(x,y)
plt.show()
plt.figure(figsize=(8,5))
plt.plot(x,y,color="red",linestyle="--",linewidth=4)
plt.title("student marks")
plt.xlabel("students")
plt.ylabel("marks")
#grid
plt.grid()
plt.show()

#legend
math=[80,90,75,95]
science=[85,88,79,91]
plt.plot(math,label="Math")
plt.plot(science,label="Science")
plt.legend()
plt.show()

#savefig
students=["Amit","Neha","Karan","Divya"]
marks=[80,90,75,95]
plt.figure(figsize=(8,5))
plt.plot(
    students,
    marks,
    color="green",
    linestyle="--",
    linewidth=3,
    marker="o",
    markersize=8,
    label="Marks"
)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.legend()
plt.savefig("student_marks.png")
plt.show()

#bar chart
students = ["Amit","Neha","Karan","Divya"]
marks = [90,85,75,95]
plt.bar(students, marks,color="red",width=0.5)
plt.show()

#horizontal bar chart
students = ["Amit","Neha","Karan","Divya"]
marks = [90,85,75,95]
plt.figure(figsize=(8,5))
plt.barh(
    students,
    marks,
    color="orange"
)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(axis="y")
plt.show()

#histogram
marks = [70,75,80,82,84,85,88,90,91,95]
plt.figure(figsize=(8,5))
plt.hist(
    marks,
    bins=5,
    color="pink"
)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid()
plt.show()

#scatter plot
height = [150,160,170,180]
weight = [45,55,65,80]
plt.scatter(height, weight,color="purple",marker="*",s=100,alpha=0.5)
plt.show()
