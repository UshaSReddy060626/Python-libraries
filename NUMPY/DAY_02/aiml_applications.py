#working with dataset
import numpy as np
data = np.array([
    [2, 70, 0],
    [5, 90, 1],
    [7, 95, 1]
])
print(data)

#fetaure matrix
X = data[:, :2]
print(X)

#label
y = data[:, 2]
print(y)

#image arrays
image = np.array([
    [10,30,50],
    [80,90,40],
    [20,60,70]
])
print(image)

#matrix operations
marks = np.array([80,20])
weights = np.array([0.7,0.3])
final = np.dot(marks,weights)
print(final)

#batch processing
marks = np.array([40,50,60,70])
new_marks = marks + 5
print(new_marks)