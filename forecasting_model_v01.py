import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the egg price dataset
df = pd.read_csv('egg_price.csv')

# Convert the 'date' column to a datetime object
df['date'] = pd.to_datetime(df['date'])

# Create a new column for the month
df['month'] = df['date'].dt.month

# Create a new column for the year
df['year'] = df['date'].dt.year

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(df[['month', 'year']], df['price'])

# Create a list of months and years for measuring performance
start_date_measuring = pd.to_datetime('1/1/2019')
end_date_measuring = pd.to_datetime('10/1/2023')
measuring_dates = pd.date_range(start_date_measuring, end_date_measuring, freq='MS')

# Create lists to store results for measuring performance
measuring_dates = measuring_dates.tolist()
measuring_prices = df.loc[df['date'].between(start_date_measuring, end_date_measuring), 'price'].tolist()

# Create a list of months and years for which to make predictions
start_date_predicting = pd.to_datetime('11/1/2023')
end_date_predicting = pd.to_datetime('10/1/2027')
prediction_dates = pd.date_range(start_date_predicting, end_date_predicting, freq='MS')

# Create lists to store results for making predictions
predicted_dates = []
predicted_prices = []

# Make predictions for each month
for date in prediction_dates:
    month = date.month
    year = date.year

    # Create a DataFrame with the input features
    prediction_data = pd.DataFrame({'month': [month], 'year': [year]})

    # Make the prediction
    prediction = model.predict(prediction_data)

    # Store the prediction results
    predicted_dates.append(date)
    predicted_prices.append(prediction[0])

    # Print the prediction result in the console
    print(f"Year: {year}, Month: {month}, Prediction: {prediction[0]}")

# Calculate evaluation metrics using the actual data for measuring performance
measuring_prices_actual = df.loc[df['date'].between(start_date_measuring, end_date_measuring), 'price']
mae_measuring = mean_absolute_error(measuring_prices_actual, measuring_prices)
mse_measuring = mean_squared_error(measuring_prices_actual, measuring_prices)
rmse_measuring = np.sqrt(mse_measuring)
r2_measuring = r2_score(measuring_prices_actual, measuring_prices)

# Print the evaluation metrics for measuring performance
print("Performance Metrics Using Measuring Period:")
print(f"Mean Absolute Error (MAE): {mae_measuring}")
print(f"Mean Squared Error (MSE): {mse_measuring}")
print(f"Root Mean Squared Error (RMSE): {rmse_measuring}")
print(f"R-squared (R2) Score: {r2_measuring}")

# Calculate evaluation metrics for the predicted period
mae_predicting = mean_absolute_error(df.loc[df['date'].between(start_date_predicting, end_date_predicting), 'price'], predicted_prices)
mse_predicting = mean_squared_error(df.loc[df['date'].between(start_date_predicting, end_date_predicting), 'price'], predicted_prices)
rmse_predicting = np.sqrt(mse_predicting)
r2_predicting = r2_score(df.loc[df['date'].between(start_date_predicting, end_date_predicting), 'price'], predicted_prices)

# Print the evaluation metrics for the predicted period
print("Performance Metrics Using Predicted Period:")
print(f"Mean Absolute Error (MAE): {mae_predicting}")
print(f"Mean Squared Error (MSE): {mse_predicting}")
print(f"Root Mean Squared Error (RMSE): {rmse_predicting}")
print(f"R-squared (R2) Score: {r2_predicting}")

# Combine the original dataset with prediction results
combined_dates = df['date'].tolist() + predicted_dates
combined_prices = df['price'].tolist() + predicted_prices

# Create a time series plot
plt.figure(figsize=(12, 6))
plt.plot(combined_dates, combined_prices, label='Actual Prices')
plt.plot(predicted_dates, predicted_prices, 'ro', label='Predicted Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Egg Price Time Series with Predictions')
plt.legend()
plt.grid(True)
plt.show()
