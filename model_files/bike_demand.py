import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

# Reading the dataset
dataset = pd.read_csv(
    r"C:\Users\olutu\ML_BIKE_DEMAND\model_files\SeoulBikeDemand.csv",
    encoding="unicode_escape",
)

# Dropping the date attribute
dataset = dataset.drop("Date", axis=1)

# Changing the variable names to improve readability
features = {
    "Rented Bike Count": "Bike Demand",
    "Hour": "Time of Day",
    "Temperature(°C)": "Temperature",
    "Humidity(%)": "Humidity",
    "Wind speed (m/s)": "Wind Speed",
    "Visibility (10m)": "Visibility",
    "Dew point temperature(°C)": "Dew Point Temperature",
    "Solar Radiation (MJ/m2)": "Solar Radiation",
    "Rainfall(mm)": "Rainfall",
    "Snowfall (cm)": "Snowfall",
    "Seasons": "Seasons",
    "Holiday": "Holiday",
    "Functioning Day": "Working Day",
}

dataset = dataset.rename(columns=features)

# Mapping the categorical variables into integers
dataset["Working Day"] = (
    dataset["Working Day"].map({"Yes": 1, "No": 0}).astype(int)
)
dataset["Holiday"] = (
    dataset["Holiday"].map({"No Holiday": 0, "Holiday": 1}).astype(int)
)
dataset["Seasons"] = (
    dataset["Seasons"]
    .map({"Winter": 1, "Spring": 2, "Summer": 3, "Autumn": 4})
    .astype(int)
)
dataset.head()

# Separating the variables into X and y, independent and dependent variables
X = dataset[
    [
        "Time of Day",
        "Temperature",
        "Humidity",
        "Wind Speed",
        "Visibility",
        "Dew Point Temperature",
        "Solar Radiation",
        "Rainfall",
        "Snowfall",
        "Seasons",
        "Holiday",
        "Working Day",
    ]
]

y = dataset["Bike Demand"]
