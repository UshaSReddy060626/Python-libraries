#import required libraries
import pandas as pd
import joblib
import pickle
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

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

#create the model
model = RandomForestClassifier(random_state=42)

#train the model
model.fit(X_train, y_train)

#save the model using joblib
joblib.dump(model, "random_forest_joblib.pkl")
print("\nModel Saved Using Joblib")

#load the model using joblib
loaded_joblib_model = joblib.load("random_forest_joblib.pkl")

#predict using the loaded joblib model
joblib_predictions = loaded_joblib_model.predict(X_test)
print("\nPredictions Using Joblib Model")
print(joblib_predictions)

#save the model using pickle
with open("random_forest_pickle.pkl", "wb") as file:
    pickle.dump(model, file)
print("\nModel Saved Using Pickle")

#load the model using pickle
with open("random_forest_pickle.pkl", "rb") as file:
    loaded_pickle_model = pickle.load(file)

#predict using the loaded pickle model
pickle_predictions = loaded_pickle_model.predict(X_test)
print("\nPredictions Using Pickle Model")
print(pickle_predictions)

#display the accuracy
accuracy = loaded_pickle_model.score(X_test, y_test)
print("\nModel Accuracy")
print(accuracy)