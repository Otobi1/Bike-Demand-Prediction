# Bike-Demand-Prediction

Data Collection

    *Source*: Data was sourced from the UCI Machine Learning Repository - [Seoul Bike Sharing Demand] (http://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand)
    
    *Description*: The repo contains a brief explanation on why it is important understand bike demand, particularly to ensure the stability of supply and improve mobiltiy comfort in rapidly urbanising contexts. 

    *Objective*: Overall objective of the analysis is to understand/predict bike demand based on specific variables 

Exploratory Data Analysis (EDA)

    *Variables and Data Types*: The dataset contain 14 attributes and 8760 observations. 10 of the attributes are of the integer or float data type while 4 are objectives or categorical data types. 

    *Independent and Dependent Variables*: All other attributes asides the bike demand (Rented Bike Count) are the predictors, while Rented Bike Count (Bike Demand) is the dependent variable 

    *Correlations*: 

    Variables Selected

    Renaming Variables for Readability

Preprocessing/Feature Engineering

    Categorical to Integers via Dummy Variables

    Correlations After Variable Mapping

    Train, Validation, Text Split

Modelling

    Regression Models

        Linear Regression

        Decision Tree Regressor

        Random Forest Regressor

        Support Vector Machine Regressor

Model Evaluation

    Mean Squared Error

    Root Mean Squared Error

Model Selection

    Hyperparameter Tuning with GridSearch CV

    Feature Importance

Model Packaging

    Pickling

Deployment

    Heroku
