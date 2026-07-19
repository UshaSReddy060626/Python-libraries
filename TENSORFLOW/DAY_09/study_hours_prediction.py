#import required libraries
import tensorflow as tf
import numpy as np

#tf.constant
a = tf.constant([[2,4],[6,8]])
print("Constant Tensor")
print(a)

#tf.variable
b = tf.Variable([[1,3],[5,7]])
print("\nVariable Tensor")
print(b)

#shape
print("\nShape")
print(a.shape)

#dtype
print("\nData Type")
print(a.dtype)

#rank
print("\nRank")
print(tf.rank(a))

#addition
print("\nAddition")
print(a + b)

#subtraction
print("\nSubtraction")
print(a - b)

#multiplication
print("\nMultiplication")
print(a * b)

#division
print("\nDivision")
print(tf.divide(a, b))

#matrix multiplication
print("\nMatrix Multiplication")
print(tf.matmul(a, b))

#reshape
print("\nReshape")
print(tf.reshape(a, (1,4)))

#transpose
print("\nTranspose")
print(tf.transpose(a))

#zeros
print("\nZeros")
print(tf.zeros((3,2)))

#ones
print("\nOnes")
print(tf.ones((3,2)))

#random normal
print("\nRandom Normal")
print(tf.random.normal((2,3)))

#random uniform
print("\nRandom Uniform")
print(tf.random.uniform((2,3)))

#range
print("\nRange")
print(tf.range(5,16))

#input data
X = np.array([[1],[2],[3],[4],[5]], dtype=float)

#output data
y = np.array([30000,40000,50000,60000,70000], dtype=float)

#build neural network
model = tf.keras.Sequential([

    #hidden layer
    tf.keras.layers.Dense(10, input_shape=(1,), activation="relu"),

    #output layer
    tf.keras.layers.Dense(1)
])

#compile model
model.compile(

    #optimizer
    optimizer="adam",

    #loss
    loss="mse",

    #metrics
    metrics=["mae"]
)

#train model
model.fit(
    X,
    y,
    epochs=150,
    batch_size=1,
    verbose=0
)

#evaluate model
loss, mae = model.evaluate(X, y, verbose=0)
print("\nLoss")
print(loss)
print("\nMAE")
print(mae)

#predict
prediction = model.predict(np.array([[6]], dtype=float))
print("\nPredicted Salary")
print(prediction)