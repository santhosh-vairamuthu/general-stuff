import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the dataset
col_names = ['Year', 'Month', 'Monthly Anomaly', 'Monthly Unc.', 'Annual Anomaly', 'Annual Unc', 'Five-Year Anomaly', 'Five-Year Unc.', 'Ten-Year Anomaly', 'Ten-Year Unc.', 'Twenty-Year Anomaly', 'Twenty-year Unc.']
temperature = pd.read_csv("Temperature.csv", header=0, names=col_names)

# Preprocess the data (if needed)

# Split dataset into features and target variable
feature_cols = ['Month', 'Monthly Anomaly', 'Monthly Unc.', 'Annual Anomaly', 'Annual Unc', 'Five-Year Anomaly', 'Five-Year Unc.', 'Ten-Year Anomaly', 'Ten-Year Unc.', 'Twenty-Year Anomaly']
X = temperature[feature_cols]  # Features
y = temperature['Twenty-year Unc.']  # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test

# Create Decision Tree regressor object
regressor = DecisionTreeRegressor()

# Train Decision Tree Regressor
regressor.fit(X_train, y_train)

# Predict the response for the test dataset
y_pred = regressor.predict(X_test)

# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)