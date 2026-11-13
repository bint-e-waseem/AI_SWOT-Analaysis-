import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import os

def forecast_sales(df):
    """
    Forecasts future sales based on historical date data using Linear Regression.
    """
    print("Initiating sales forecasting model...")

    # Ensure Date column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Aggregate sales by date
    daily_sales = df.groupby('Date')['Sales'].sum().reset_index()
    
    # Convert dates to numerical format (ordinal) for the model
    daily_sales['Date_Ordinal'] = daily_sales['Date'].map(pd.Timestamp.toordinal)
    
    # Define features (X) and target (y)
    X = daily_sales[['Date_Ordinal']]
    y = daily_sales['Sales']
    
    # Initialize and train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Make predictions on the historical data to evaluate
    predictions = model.predict(X)
    
    # Calculate evaluation metrics
    mae = mean_absolute_error(y, predictions)
    rmse = np.sqrt(mean_squared_error(y, predictions))
    
    print(f"Model Evaluation - MAE: {mae:.2f}, RMSE: {rmse:.2f}")
    
    # Forecast for the next 30 days
    last_date = daily_sales['Date'].max()
    future_dates = [last_date + pd.Timedelta(days=i) for i in range(1, 31)]
    future_ordinals = np.array([d.toordinal() for d in future_dates]).reshape(-1, 1)
    
    future_predictions = model.predict(future_ordinals)
    
    # Create a dataframe for the forecast
    forecast_df = pd.DataFrame({
        'Date': future_dates,
        'Predicted_Sales': future_predictions
    })
    
    # Save the forecast to the processed data folder
    os.makedirs('data/processed', exist_ok=True)
    forecast_df.to_csv('data/processed/sales_forecast.csv', index=False)
    
    print("Forecasting completed. Results saved to 'data/processed/sales_forecast.csv'.")
    return forecast_df

if __name__ == "__main__":
    file_path = "data/processed/cleaned_supermarket_data.csv"
    
    if os.path.exists(file_path):
        print("Loading cleaned data...")
        data = pd.read_csv(file_path)
        forecast_sales(data)
    else:
        print(f"Error: File not found at {file_path}. Please run cleaner.py first.")