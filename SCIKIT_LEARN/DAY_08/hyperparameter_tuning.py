#import required libraries
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
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

#parameters for grid search
parameters = {
    "n_estimators": [50, 100, 150],
    "max_depth": [3, 5, 7]
}

#apply gridsearchcv
grid_search = GridSearchCV(
    estimator=model,
    param_grid=parameters,
    cv=5
)
grid_search.fit(X_train, y_train)
print("\nGrid Search Best Parameters")
print(grid_search.best_params_)
print("\nGrid Search Best Score")
print(grid_search.best_score_)

#apply randomizedsearchcv
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=parameters,
    n_iter=4,
    cv=5,
    random_state=42
)
random_search.fit(X_train, y_train)
print("\nRandom Search Best Parameters")
print(random_search.best_params_)
print("\nRandom Search Best Score")
print(random_search.best_score_)