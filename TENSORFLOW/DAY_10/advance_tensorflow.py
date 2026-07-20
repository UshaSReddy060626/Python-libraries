#import required libraries
import tensorflow as tf
import numpy as np

#input data
X = np.array([[0],[1],[2],[3],[4],[5]], dtype=np.float32)

#binary output
y = np.array([0,0,0,1,1,1], dtype=np.float32)

#build neural network
model = tf.keras.Sequential([

#input layer
    tf.keras.layers.Input(shape=(1,)),

#hidden layer
    tf.keras.layers.Dense(8, activation="sigmoid"),

#output layer
    tf.keras.layers.Dense(1, activation="sigmoid")
])

#compile model
model.compile(

#optimizer
    optimizer="sgd",

#loss function
    loss="binary_crossentropy",

#metrics
    metrics=["accuracy"]
)

#train model
model.fit(
    X,
    y,
    epochs=100,
    batch_size=1,
    verbose=0
)

#evaluate model
loss, accuracy = model.evaluate(X, y, verbose=0)
print("Loss:", loss)
print("Accuracy:", accuracy)

#save model
model.save("binary_classifier.keras")

#load saved model
loaded_model = tf.keras.models.load_model("binary_classifier.keras")

#predict
prediction = loaded_model.predict(
    np.array([[2.5],[4.5]], dtype=np.float32)
)

print("Predictions:")
print(prediction)