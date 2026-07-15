import matplotlib.pyplot as plt
study_hours = [1,2,3,4,5,6,7,8]
marks = [35,45,55,65,75,82,90,97]
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.scatter(study_hours, marks,
            color="purple",
            marker="o",
            s=120,
            alpha=0.8)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid()
plt.subplot(1,2,2)
plt.plot(study_hours, marks,
         color="blue",
         marker="*",
         linewidth=2,
         label="Marks")
plt.title("Marks Trend")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("aiml_visualization.png")
plt.show()