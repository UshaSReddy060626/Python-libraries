#import required libraries
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

#load the breast cancer dataset
cancer = load_breast_cancer()

#create a dataframe
df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
df["Target"] = cancer.target
print("Breast Cancer Dataset")
print(df.head())

#features and labels
X = cancer.data
y = cancer.target

#split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#create the pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", SVC())
])

#train the pipeline
pipeline.fit(X_train, y_train)

#predict using the pipeline
predictions = pipeline.predict(X_test)
print("\nPredicted Values")
print(predictions)

#display the accuracy
accuracy = pipeline.score(X_test, y_test)
print("\nPipeline Accuracy")
print(accuracy)