import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df["Wine_Class"] = wine.target
print("Wine Dataset")
print(df.head())
X = wine.data
y = wine.target
print("\nFeatures Shape:", X.shape)
print("Labels Shape:", y.shape)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)
standard = StandardScaler()
X_train_standard = standard.fit_transform(X_train)
X_test_standard = standard.transform(X_test)
print("\nStandardScaler Applied")
print(X_train_standard[:3])
minmax = MinMaxScaler()
X_train_minmax = minmax.fit_transform(X_train)
X_test_minmax = minmax.transform(X_test)
print("\nMinMaxScaler Applied")
print(X_train_minmax[:3])
quality = ["Premium", "Standard", "Economy", "Premium"]
encoder = LabelEncoder()
encoded = encoder.fit_transform(quality)
print("\nLabel Encoder")
print(encoded)
model = LogisticRegression(max_iter=1000)
model.fit(X_train_standard, y_train)
print("\nModel Trained Successfully")
predictions = model.predict(X_test_standard)
print("\nPredicted Classes:")
print(predictions)
print("\nActual Classes:")
print(y_test)
accuracy = model.score(X_test_standard, y_test)
print("\nModel Accuracy:", accuracy)