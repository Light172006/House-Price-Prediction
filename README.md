# 🏠 House Price Prediction Web App

An end-to-end Machine Learning-based House Price Prediction system built using Python.
The application predicts house prices based on key property features such as location, area, number of bedrooms (BHK), floor information, and other relevant attributes.

The project demonstrates the full ML lifecycle — from data preprocessing and feature engineering to model training, evaluation, and deployment using Streamlit.

## 🚀 Project Overview

House price prediction is a classic real-world regression problem. This project focuses on building a reliable and well-evaluated model using proper machine learning practices such as cross-validation, hyperparameter tuning, and leakage prevention.

Multiple regression models were trained and compared, and the best-performing model was deployed as an interactive web application.

## 🧠 Machine Learning Pipeline

Data Cleaning & Preprocessing

Handled missing values and inconsistent entries

Processed categorical and numerical features

Proper handling of floor information (current floor & total floors)

Feature Engineering

Removed leakage-prone features (e.g., price per sqft)

Encoded categorical variables

Selected relevant predictors for better generalization

Model Training & Evaluation

Models tested:

Linear Regression

Lasso Regression

Ridge Regression

K-Nearest Neighbors (KNN)

Decision Tree Regressor

Random Forest Regressor (Final Model)

Hyperparameter tuning using GridSearchCV

Performance evaluation using Cross-Validation (R² score)

## 📊 Model Performance

Final Model: Random Forest Regressor

Cross-Validation R² Score: ~ 0.74

Indicates strong predictive performance and good generalization on unseen data

## 🖥️ Web Application

An interactive Streamlit web app allows users to:

Enter property details

Get real-time house price predictions

Interact with a clean and user-friendly UI

## 🛠️ Tech Stack

Python

NumPy

Pandas

Scikit-learn

Streamlit

Joblib
