# Bike-Demand-Prediction

## Data Collection

*Source* Data was sourced from the UCI Machine Learning Repository [Seoul-Bike-Sharing-Demand](https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand)

*Description*: The repo contains a brief explanation on why it is important understand
 bike demand, particularly to ensure the stability of supply and improve mobiltiy
 comfort in rapidly urbanising contexts.

*Objective*: Overall objective of the analysis is to understand/predict bike demand
based on specific variables

## Exploratory Data Analysis (EDA)

*Data Loading*: Data was loaded into the Googl Colab notebook using the'!wget'
command and directly read into a pandads dataframe using 'pd.read_csv'. A copy of
the data was made, so we can go back to a clean original version of the data at
any point.

*Variables and Data Types*: Using 'data.sample(10)', a subset of the data was printed
and the variables were explored. 'data.shape' revealed that the dataset contains
14 attributes and 8760 observations. Using 'data.info()', the info about the dataset
was explored. 10 of the attributes are of the integer or float data type while 4
are objectives or categorical data types. 'data.isnull().sum()' revealed that there
is no missing observation for any of the variables.

*Independent and Dependent Variables*: All other attributes asides the bike demand
 (Rented Bike Count) are the predictors, while Rented Bike Count (Bike Demand)
 is the dependent variable

*Correlations*: Grouped into varaibles that are positively correlated with the
bike demand (i.e as these variables increase or improve, bike demand increases)
and variables that are negatively correlated with bike demand (i.e as these variables
increase or the situation worsens, bike demand decreases). These variables can
be further categorised as being strongly correlated or not strongly correlated.

*Variables Selection and Renaming*: All varaibles were selected except the date variable
 (at least for now). And the variables were renamed to improve readability.

## Preprocessing/Feature Engineering/Dummy Variables

*Categorical to Integers via Dummy Variables*: The categorical variables include
Seasons; Spring, Autumn, Summer, Winter, Functioning Day; Yes or No and Holiday
Yes or No. These categorical variables were mapped into integers using the
'pd.get_dummies' function of pandas. To prevent the dummy variable trap (multicolinearity),
the first column of each of the dummy variables were dropped.

*Correlations After Variable Mapping*: revealed 'Time of Day', 'Solar Radiation',
'Temperature', 'Summer' and a 'Working Day' had a strong positive correlation
with increase bike demand.

*Standardisation and Data Split*: As the variables in the dataset had varying
orders of magnitude, it was important to standardise the dataset using the
sci-kit learns' StandardScaler function to make the mean 0 and the variance 1.
After that, the data was split into 2 parts, the train and the test split.

## Modelling and Evaluation

*Regression Models*: Several regression models were used. They were fitted and
evaluated based on the coefficient of determination (R2), difference between
the actual bike demand (y_test) and predicted bike demand (y_pred), mean squared
error and the root mean squared error.

- *Linear Regression*: only 54% of the variation in the bike demand can be
   explained by the variation in the input features. Exploration of the actual
   and predicted values indicates a wide variance. MSE significantly high and
   RMSE in the same region.

- *Decision Tree Regressor*: Actual and predicted values for bike demand are
   reasonably close, with 72% of the variations in bike demand explanable by
   variation in the input features. MSE is 0, indicating a perfect prediction
   model and RMSE reasonably within the range.

- *Random Forest Regressor*: Actual and predicted values for bike demand also
   reasonably close. 86% of the variation in bike demand explanable by the variation
   in the input features. MSE is 0, indicating a perfect prediction of the model
   and RMSE reasonably close.

- *Support Vector Machine Regressor*: Performed poorly than all the other models
   with only about 51% of the variations in bike demand explanable by the variation
   in the input features. Although the MSE is 0, the difference between the
   actual and the predicted values were significant.

## Model Selection

*Hyperparameter Tuning with GridSearch CV and Feature Importance*: Based on
the performance of the models,the hyperparameter tuning was done using the
Random Forest Regressor and an array of parameters in a grid. The grid search
revealed the max optimal features to be 8 and the number of estimators to be
30 based on the mean scores of the param categories. the feature importance
also computed and ranked.

## Model Packaging

*Pickling*: the best estimator from the grid search consists of the best model
this is pickled and packaged for deployment.

## Deployment

*Heroku*: [Bike Demand App](https://bike-demand-pred.herokuapp.com/)
