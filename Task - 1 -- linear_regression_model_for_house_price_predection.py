# -*- coding: utf-8 -*-
"""linear regression model for house price predection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B1mN1OjnChiqY5hOvbHnRJ03vf3E4BBf
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the training and testing datasets
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Display the first few rows of the datasets
print("Training Data:")
print(train_data.head())

print("\nTesting Data:")
print(test_data.head())

# Define features and target variable for training data
X_train = train_data[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'HalfBath']]
y_train = train_data['SalePrice']

# Define features for testing data (target variable is not present in test data)
X_test = test_data[['GrLivArea', 'BedroomAbvGr', 'FullBath', 'HalfBath']]

# Create the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Example new data: a house with 2500 square feet of living area, 4 bedrooms, 2 full bathrooms, and 1 half bathroom
new_data = np.array([[2500, 4, 2, 1]])

# Predict the price
predicted_price = model.predict(new_data)
print(f'Predicted Price for a house with 2500 sqft, 4 bedrooms, 2 full bathrooms, and 1 half bathroom: {predicted_price[0]}')

# Save the predictions to a CSV file
submission = pd.DataFrame({'Id': test_data['Id'], 'SalePrice': y_pred})
submission.to_csv('sample_submission.csv', index=False)