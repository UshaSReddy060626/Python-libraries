#import required libraries
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

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

#create the model
model = DecisionTreeClassifier(random_state=42)

#apply 5-fold cross validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

#display the accuracy of each fold
print("\nAccuracy of Each Fold")
print(scores)

#display the average accuracy
print("\nMean Accuracy")
print(scores.mean())