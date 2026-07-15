import matplotlib.pyplot as plt
students = ["Amit","Neha","Karan","Divya"]
maths = [88,92,76,95]
science = [85,90,80,91]
plt.figure(figsize=(8,5))
plt.plot(students, maths, color="blue", marker="o", linewidth=2, label="Maths")
plt.plot(students, science, color="red", marker="s", linestyle="--", linewidth=2, label="Science")
plt.title("Student Performance")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.legend()
plt.savefig("student_performance.png")
plt.show()

