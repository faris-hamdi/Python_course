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

# Create a list of months and years for which to make predictions
start_date = pd.to_datetime('1/1/2022')
end_date = pd.to_datetime('10/1/2027')
date_range = pd.date_range(start_date, end_date, freq='MS')

# Create lists to store results for plotting
all_dates = df['date'].tolist()
all_prices = df['price'].tolist()
predicted_dates = []
predicted_prices = []

# Make predictions for each month
for date in date_range:
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

# Calculate evaluation metrics using the overlapping period
overlap_start_date = pd.to_datetime('1/1/2022')
overlap_end_date = pd.to_datetime('10/1/2023')
overlap_actual_prices = df.loc[df['date'].between(overlap_start_date, overlap_end_date), 'price']
overlap_predicted_prices = predicted_prices[:12]

mae = mean_absolute_error(overlap_actual_prices, overlap_predicted_prices)
mse = mean_squared_error(overlap_actual_prices, overlap_predicted_prices)
rmse = np.sqrt(mse)
r2 = r2_score(overlap_actual_prices, overlap_predicted_prices)

# Print the evaluation metrics for the overlapping period
print("Performance Metrics Using Overlapping Period:")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R2) Score: {r2}")

# Combine the original dataset with prediction results
combined_dates = all_dates + predicted_dates
combined_prices = all_prices + predicted_prices

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
