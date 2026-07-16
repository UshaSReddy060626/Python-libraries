#feature comparison
import matplotlib.pyplot as plt
departments=["AI","Web","Cloud","Data"]
salary=[18,12,15,16]
plt.bar(departments,salary,color="green")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary (LPA)")
plt.grid(axis="y")
plt.show()

#class distribution
classes=["Cat","Dog","Bird"]
count=[300,500,200]
plt.pie(
    count,
    labels=classes,
    autopct="%1.1f%%"
)
plt.title("Class Distribution")
plt.show()

#prediction vs actual
actual=[50,60,70,80,90]
predicted=[52,58,69,82,91]
plt.scatter(actual,predicted,color="blue")
plt.title("Prediction vs Actual")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.grid()
plt.show()

#training loss curve
epochs=[1,2,3,4,5]
loss=[0.9,0.7,0.5,0.3,0.2]
plt.plot(
    epochs,
    loss,
    marker="o",
    color="red"
)
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid()
plt.show()

#accuracy curve
epochs=[1,2,3,4,5]
accuracy=[60,72,80,88,93]
plt.plot(
    epochs,
    accuracy,
    marker="*",
    color="green"
)
plt.title("Training Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
plt.grid()
plt.show()

