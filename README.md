# Myocardial-Infarction

## Overview
* A multi-classification problem, to detect different type of myocardial infarction based on observed variables
* It's a high dimensional dataset... with a number of discrete, continuous, and categorical variables
* Data was analyzed and feature-enginered to be made model-worthy
* Optimized Base and Ensemble Learner Algorithms to build a model
* Created a tool for early detection of Myocardial Infarction
* Built a client facing API using fastapi and colabcode

## Code and Resources used
* Python version : Python 3.7
* Packages : pandas, numpy, matplotlib, seaborn, sklearn, imblearn, pickle, fastapi, flask, django

## Project Walk-through

### 1. Back-end code 
* Dataset : Dataset was read using pandas library.
* Domain Knowledge : Each column variables was studied and their importance was found.
* Data Cleaning : Data was checked for null values, and imputed based on the type of data.
* Normalizing : The input float -continuous- values, as the scales of different variables are widely spread and ununiform, were scaled.
* Feature Selection : Based on the concept of chi2, weight of each column was detected; Features are selected based on the values.
* The Split : The dataset was divided - predictor(X) and target variable(y). Also, train_test_split was implemented.
* Balancing techniques : Training dataset was checked for balance; imbalance was detected. Balancing was achieved by implementing smote.
* Predict-worthy Algorithms : Decision Tree, KNN, Random Forest.
* RandomForestClassifier gave a maximum accuracy for correct prediction of patients' records with utmost ability to categorize the patient.

### 2. Deployment
* Deployment was successful
* Deployment was done with the help of heroku app.
* For an interactive user experience, web-app can be viewed at https://myocardial-complication.herokuapp.com/
