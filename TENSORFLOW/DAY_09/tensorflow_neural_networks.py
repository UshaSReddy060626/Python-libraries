#import required libraries
import tensorflow as tf
import numpy as np

#input data
X = np.array([[1],[2],[3],[4],[5]], dtype=float)

#output data
y = np.array([30,40,50,60,70], dtype=float)

#build neural network
model = tf.keras.Sequential([

    #hidden layer
    tf.keras.layers.Dense(8, input_shape=(1,), activation="relu"),

    #output layer
    tf.keras.layers.Dense(1)
])

#compile model
model.compile(

    #optimizer
    optimizer="adam",

    #loss function
    loss="mse",

    #evaluation metric
    metrics=["mae"]
)

#train model
model.fit(

    X,
    y,

    #number of training cycles
    epochs=100,

    #samples per batch
    batch_size=1,
    verbose=0
)

#evaluate model
loss, mae = model.evaluate(X, y, verbose=0)
print("Loss:", loss)
print("MAE:", mae)

#predict new value
prediction = model.predict(np.array([[6]], dtype=float))
print("Prediction:", prediction)