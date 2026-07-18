#import required libraries
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

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

#decision tree model
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)
dt_predictions = decision_tree.predict(X_test)
print("\nDecision Tree")
print("Accuracy :", accuracy_score(y_test, dt_predictions))
print("Precision:", precision_score(y_test, dt_predictions))
print("Recall   :", recall_score(y_test, dt_predictions))
print("F1 Score :", f1_score(y_test, dt_predictions))
print("Confusion Matrix")
print(confusion_matrix(y_test, dt_predictions))
print("Classification Report")
print(classification_report(y_test, dt_predictions))

#random forest model
random_forest = RandomForestClassifier(random_state=42)
random_forest.fit(X_train, y_train)
rf_predictions = random_forest.predict(X_test)
print("\nRandom Forest")
print("Accuracy :", accuracy_score(y_test, rf_predictions))
print("Precision:", precision_score(y_test, rf_predictions))
print("Recall   :", recall_score(y_test, rf_predictions))
print("F1 Score :", f1_score(y_test, rf_predictions))
print("Confusion Matrix")
print(confusion_matrix(y_test, rf_predictions))
print("Classification Report")
print(classification_report(y_test, rf_predictions))

#support vector machine model
svm = SVC()
svm.fit(X_train, y_train)
svm_predictions = svm.predict(X_test)
print("\nSupport Vector Machine")
print("Accuracy :", accuracy_score(y_test, svm_predictions))
print("Precision:", precision_score(y_test, svm_predictions))
print("Recall   :", recall_score(y_test, svm_predictions))
print("F1 Score :", f1_score(y_test, svm_predictions))
print("Confusion Matrix")
print(confusion_matrix(y_test, svm_predictions))
print("Classification Report")
print(classification_report(y_test, svm_predictions))

#k-nearest neighbors model
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_predictions = knn.predict(X_test)
print("\nK-Nearest Neighbors")
print("Accuracy :", accuracy_score(y_test, knn_predictions))
print("Precision:", precision_score(y_test, knn_predictions))
print("Recall   :", recall_score(y_test, knn_predictions))
print("F1 Score :", f1_score(y_test, knn_predictions))
print("Confusion Matrix")
print(confusion_matrix(y_test, knn_predictions))
print("Classification Report")
print(classification_report(y_test, knn_predictions))