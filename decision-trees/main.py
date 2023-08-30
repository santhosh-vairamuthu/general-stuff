import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
col_names = ['Year', 'Month', 'Monthly Anomaly', 'Monthly Unc.', 'Annual Anomaly', 'Annual Unc', 'Five-Year Anomaly', 'Five-Year Unc.', 'Ten-Year Anomaly', 'Ten-Year Unc.', 'Twenty-Year Anomaly', 'Twenty-year Unc.']
temperature = pd.read_csv("Temperature.csv", header=0, names=col_names)

# Preprocess the data (if needed)

# Create a new column "Class" for classification labels
temperature['Class'] = 'Normal'

# Apply multiple constraints for classification
temperature.loc[(temperature['Monthly Anomaly'] > 0.2) & (temperature['Annual Anomaly'] > 0.2), 'Class'] = 'Anomaly 1'
temperature.loc[(temperature['Monthly Anomaly'] > 0.5) & (temperature['Annual Anomaly'] > 0.5), 'Class'] = 'Anomaly 2'
temperature.loc[temperature['Monthly Anomaly'] < -0.2, 'Class'] = 'Below Normal'

# Split dataset into features and target variable
feature_cols = ['Year', 'Month', 'Monthly Anomaly', 'Monthly Unc.', 'Annual Anomaly', 'Annual Unc', 'Five-Year Anomaly', 'Five-Year Unc.', 'Ten-Year Anomaly', 'Ten-Year Unc.', 'Twenty-Year Anomaly', 'Twenty-year Unc.']
X = temperature[feature_cols]  # Features
y = temperature['Class']  # Target variable

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test

# Create Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifier
clf.fit(X_train, y_train)

# Predict the response for the test dataset
y_pred = clf.predict(X_test)

# Calculate and print accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
