# 📅 Day 08 – Python Libraries: Scikit-learn

## 📖 Overview

Today I learned advanced **Scikit-learn** concepts, including classification algorithms, cross validation, hyperparameter tuning, pipelines, and saving machine learning models using **joblib** and **pickle**. These concepts are essential for building, evaluating, and optimizing machine learning models.

---

# 📚 Topics Covered

## 🌳 Machine Learning Algorithms

* Decision Tree (`DecisionTreeClassifier`)
* Random Forest (`RandomForestClassifier`)
* Support Vector Machine (`SVC`)
* k-Nearest Neighbors (`KNeighborsClassifier`)

## 📈 Model Evaluation

* `fit()`
* `predict()`
* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

## 🔄 Model Selection

* Cross Validation
* `cross_val_score()`
* K-Fold Validation
* Mean Accuracy

## ⚙️ Hyperparameter Tuning

* `GridSearchCV`
* `RandomizedSearchCV`
* Best Parameters
* Best Score

## 🔗 Pipelines

* `Pipeline`
* `StandardScaler`
* `Pipeline.fit()`
* `Pipeline.predict()`
* `Pipeline.score()`

## 💾 Saving Models

* `joblib.dump()`
* `joblib.load()`
* `pickle.dump()`
* `pickle.load()`

---

# 💻 Programs Practiced

### ✅ Program 1 – Machine Learning Algorithms & Evaluation

* Loaded the Breast Cancer dataset
* Trained Decision Tree, Random Forest, SVM, and k-NN models
* Predicted test data
* Evaluated models using:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix
  * Classification Report

### ✅ Program 2 – Cross Validation

* Applied 5-Fold Cross Validation
* Calculated accuracy for each fold
* Computed the mean accuracy

### ✅ Program 3 – Hyperparameter Tuning

* Applied `GridSearchCV`
* Applied `RandomizedSearchCV`
* Identified the best parameters
* Compared the best model scores

### ✅ Program 4 – Pipeline

* Built a Pipeline using `StandardScaler` and `SVC`
* Trained the pipeline
* Predicted test data
* Evaluated pipeline accuracy

### ✅ Program 5 – Saving Models

* Trained a Random Forest model
* Saved the trained model using `joblib`
* Loaded the saved model using `joblib`
* Saved the trained model using `pickle`
* Loaded the saved model using `pickle`
* Used the loaded models to make predictions

---

# 🎯 What I Learned

* Built and compared multiple machine learning classification models.
* Evaluated model performance using standard classification metrics.
* Used Cross Validation to obtain more reliable performance estimates.
* Applied Hyperparameter Tuning to improve model performance.
* Built Pipelines to combine preprocessing and model training into a single workflow.
* Saved and reloaded trained machine learning models for future use.

---

# 🚀 Day 8 Summary

Today, I completed the advanced concepts of **Scikit-learn** by learning machine learning algorithms, model evaluation, cross validation, hyperparameter tuning, pipelines, and model persistence. These skills are fundamental for developing, evaluating, optimizing, and deploying machine learning models in real-world AI/ML applications.

**✅ Scikit-learn Completed Successfully**

## ✅ Day 08 Complete