# -*- coding: utf-8 -*-
"""linear_regression.py
"""

# Implementation

# Train the model

# 1. Load and split the Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv('/Users/user/Desktop/HousingData.csv')

# Fill missing values with the median of each column
data_filled = data.fillna(data.median())

# Separate the features and the target variable
X = data_filled.drop('MEDV', axis=1)
y = data_filled['MEDV']

# Adding a column of ones to X to include an intercept in the model
X = np.c_[np.ones(X.shape[0]), X]

# Split the data into training and testing sets (90% training, 10% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# 2. Train the Model Using Normal Equation

beta = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)

# Evaluate the results

# 1. Make Predictions and Evaluate the Model

# Function to predict using the calculated beta
def predict(X, beta):
    return X.dot(beta)

# Predicting on training and test datasets
y_train_pred = predict(X_train, beta)
y_test_pred = predict(X_test, beta)

# Evaluating the model
# Function to calculate R2
def r_squared(y, y_pred):
    RSS = np.sum((y - y_pred) ** 2)
    TSS = np.sum((y - np.mean(y)) ** 2)
    return 1 - RSS / TSS

# Function to calculate RSE
def RSE(y, y_pred):
    RSS = np.sum((y - y_pred) ** 2)
    RSE = np.sqrt(RSS / (len(y) - 2))
    return RSE

train_rse = RSE(y_train, y_train_pred)
test_rse = RSE(y_test, y_test_pred)
train_r2 = r_squared(y_train, y_train_pred)
test_r2 = r_squared(y_test, y_test_pred)

print("Training RSE:", train_rse)
print("Test RSE:", test_rse)
print("Training Coefficient of determination (r2):", train_r2)
print("Test Coefficient of determination (r2):", test_r2)

# 3. Choose different training/test ratios

# List of test sizes for different train/test splits
test_sizes = [0.20, 0.30, 0.50]

# Iterate over different test sizes
for test_size in test_sizes:
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Train the Model Using Normal Equation
    beta = np.linalg.inv(X_train.T.dot(X_train)).dot(X_train.T).dot(y_train)

    # Make Predictions
    y_train_pred = predict(X_train, beta)
    y_test_pred = predict(X_test, beta)

    # Evaluate the model
    train_rse = RSE(y_train, y_train_pred)
    test_rse = RSE(y_test, y_test_pred)
    train_r2 = r_squared(y_train, y_train_pred)
    test_r2 = r_squared(y_test, y_test_pred)

    print("\n")
    print(f"Results for test size {test_size * 100}%:")
    print("Training RSE:", train_rse)
    print("Test RSE:", test_rse)
    print("Training Coefficient of determination (r2):", train_r2)
    print("Test Coefficient of determination (r2):", test_r2)
    print("\n")

