# Bike-Demand-Prediction

## Data Collection

    *Source* Data was sourced from the UCI Machine Learning Repository -
    [Seoul-Bike-Sharing-Demand]:<https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand>

    *Description*: The repo contains a brief explanation on why it is important
    understand bike demand, particularly to ensure the stability of supply and
    improve mobiltiy comfort in rapidly urbanising contexts.

    *Objective*: Overall objective of the analysis is to understand/predict bike
    demand based on specific variables

## Exploratory Data Analysis (EDA)

    *Data Loading*: Data was loaded into the Googl Colab notebook using the
    '!wget' command and directly read into a pandads dataframe using 'pd.read_csv'.
    A copy of the data was made, so we can go back to a clean original version 
    of the data at any point. 

    *Variables and Data Types*: Using 'data.sample(10)', a subset of the data was
    printed and the variables were explored. 'data.shape' revealed that the dataset
    contains 14 attributes and 8760 observations. Using 'data.info()', the info 
    about the dataset was explored. 10 of the attributes are of the integer or 
    float data type while 4 are objectives or categorical data types. 'data.isnull().sum()
    revealed that there is no missing observation for any of the variables.

    *Independent and Dependent Variables*: All other attributes asides the bike
    demand (Rented Bike Count) are the predictors, while Rented Bike Count
    (Bike Demand) is the dependent variable

    *Correlations*:

    Variables Selected

    Renaming Variables for Readability

## Preprocessing/Feature Engineering/Dummy Variables

    Categorical to Integers via Dummy Variables  (Using dummy variables 
    instead of mapping variables, also avoiding dummy variable traps, multicollinearity)

    Correlations After Variable Mapping

    Train, Validation, Text Split

## Modelling

    Regression Models

        Linear Regression

        Decision Tree Regressor

        Random Forest Regressor

        Support Vector Machine Regressor

## Model Evaluation

    Mean Squared Error

    Root Mean Squared Error

## Model Selection

    Hyperparameter Tuning with GridSearch CV

    Feature Importance

## Model Packaging

    Pickling

## Deployment

    Heroku
