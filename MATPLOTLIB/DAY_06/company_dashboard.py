import matplotlib.pyplot as plt
departments = ["AI","Web","Cloud","Data"]
employees = [40,25,30,35]
projects = [12,8,10,15]
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.bar(departments, employees, color="skyblue")
plt.title("Employees in Departments")
plt.xlabel("Departments")
plt.ylabel("Employees")
plt.grid(axis="y")
plt.subplot(1,2,2)
plt.plot(
    departments,
    projects,
    color="red",
    linestyle="--",
    marker="o",
    markersize=8,
    linewidth=2,
    label="Projects"
)
plt.title("Projects Completed")
plt.xlabel("Departments")
plt.ylabel("Projects")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("company_dashboard.png")
plt.show()