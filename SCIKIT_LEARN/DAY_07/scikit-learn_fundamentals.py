#Import required libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression

#Load the built-in iris dataset
iris = load_iris()

#Convert it into a pandas dataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target
df["Flower"] = iris.target
print("Iris Dataset")
print(df.head())

#feature
X = iris.data

#label
y = iris.target
print("\nFeatures Shape:", X.shape)
print("Labels Shape:", y.shape)

#train test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("\nTraining Data:", X_train.shape)
print("Testing Data :", X_test.shape)

# StandardScaler 
standard = StandardScaler()
X_train_standard = standard.fit_transform(X_train)
X_test_standard = standard.transform(X_test)
print("\nStandardScaler Applied")
print(X_train_standard[:3])


# MinMaxScaler changes all values
minmax = MinMaxScaler()
X_train_minmax = minmax.fit_transform(X_train)
X_test_minmax = minmax.transform(X_test)
print("\nMinMaxScaler Applied")
print(X_train_minmax[:3])


# Converts text labels into numbers
flowers = ["Setosa", "Versicolor", "Virginica", "Setosa"]
encoder = LabelEncoder()
encoded = encoder.fit_transform(flowers)
print("\nLabel Encoder")
print(encoded)

# Create the model
model = LogisticRegression()

# Train the model using training data
model.fit(X_train, y_train)
print("\nModel Training Completed")

# Predict flower types for testing data
predictions = model.predict(X_test)
print("\nPredicted Labels")
print(predictions[:10])

#score
accuracy = model.score(X_test, y_test)
print("\nModel Accuracy:", accuracy)