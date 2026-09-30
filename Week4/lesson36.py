# PROJECT PHOENIX
# Week 4 — Lesson 36: Machine Learning Fundamentals

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score
)


# --------------------------------------------------
# 1. Create a Simple Healthcare Dataset
# --------------------------------------------------

data = {
    "Age": [25, 30, 35, 40, 45, 50, 55, 60],
    "BMI": [22, 24, 25, 27, 28, 30, 31, 33],
    "Glucose": [90, 95, 100, 110, 125, 140, 155, 170],
    "Diabetes": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print(df)


# --------------------------------------------------
# 2. Separate Features (X) and Target (y)
# --------------------------------------------------

X = df[["Age", "BMI", "Glucose"]]

y = df["Diabetes"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)


# --------------------------------------------------
# 3. Split Data into Training and Testing Sets
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print("\nTraining features:")
print(X_train)

print("\nTesting features:")
print(X_test)

print("\nTraining target:")
print(y_train)

print("\nTesting target:")
print(y_test)


# --------------------------------------------------
# 4. Create the Machine Learning Model
# --------------------------------------------------

model = LogisticRegression()


# --------------------------------------------------
# 5. Train the Model
# --------------------------------------------------

model.fit(X_train, y_train)


# --------------------------------------------------
# 6. Make Predictions on Unseen Data
# --------------------------------------------------

predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)


# --------------------------------------------------
# 7. Calculate Accuracy
# --------------------------------------------------

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:")
print(accuracy)


# --------------------------------------------------
# 8. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(cm)


# --------------------------------------------------
# 9. Calculate Precision
# --------------------------------------------------

precision = precision_score(y_test, predictions)

print("\nPrecision:")
print(precision)


# --------------------------------------------------
# 10. Calculate Recall / Sensitivity
# --------------------------------------------------

recall = recall_score(y_test, predictions)

print("\nRecall:")
print(recall)


# --------------------------------------------------
# 11. Calculate Specificity
# --------------------------------------------------

tn, fp, fn, tp = confusion_matrix(
    y_test,
    predictions
).ravel()

specificity = tn / (tn + fp)

print("\nSpecificity:")
print(specificity)