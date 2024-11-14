# -*- coding: utf-8 -*-
"""Historical_prices.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uRl6N_PNIkAb2cEYoXKQzA96gyY16m_k
"""

#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Loading the CSV file into a DataFrame
df = pd.read_csv('/content/drive/MyDrive/final project/historical_prices_.csv')

# Displaying the first few rows of the DataFrame to understand its structure
df.head()

from google.colab import drive
drive.mount('/content/drive')

# Converting the 'Date' column to datetime format for better handling
df['Date'] = pd.to_datetime(df['Date'])

# Sorting the DataFrame by date to ensure chronological order
df.sort_values('Date', inplace=True)

# Displaying basic statistics of the numerical columns
df.describe()

# Plotting the closing prices over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
plt.title('GBP/USD Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.legend()
plt.show()

# Calculating the daily returns
df['Daily Return'] = df['Close'].pct_change()

# Daily returns over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Daily Return'], label='Daily Return', color='green')
plt.title('GBP/USD Daily Returns Over Time')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.grid(True)
plt.legend()
plt.show()

# Analysis of GBP/USD Exchange Rate Data

# Calculating the overall percentage change in the closing price from the start to the end of the dataset
start_price = df['Close'].iloc[0]
end_price = df['Close'].iloc[-1]
overall_change = ((end_price - start_price) / start_price) * 100

# Calculating the average daily return
average_daily_return = df['Daily Return'].mean()

# Calculating the standard deviation of daily returns to understand volatility
volatility = df['Daily Return'].std()

# Determining the date with the highest closing price
highest_closing_date = df.loc[df['Close'].idxmax(), 'Date']

# Determining the date with the lowest closing price
lowest_closing_date = df.loc[df['Close'].idxmin(), 'Date']

(overall_change, average_daily_return, volatility, highest_closing_date, lowest_closing_date)

# Data Preprocessing
# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])
# Sort data by date
df.sort_values('Date', inplace=True)
# Set 'Date' as index
df.set_index('Date', inplace=True)

# Handle missing values
# Assuming 'Close' is the main column of interest, fill missing values with the previous value
df['Close'].fillna(method='ffill', inplace=True)

# Calculate daily percentage change
df['Daily Change %'] = df['Close'].pct_change() * 100

df.head()

### Step 2: Analytical Techniques
#Now that the data is preprocessed, I will proceed with the analytical techniques:

#1. **Trend Analysis**: Calculate moving averages (20-day and 50-day) to identify trends.
#2. **Volatility Analysis**: Calculate Bollinger Bands and the Relative Strength Index (RSI) to assess volatility.

#Let's calculate the moving averages first.

# Calculate moving averages
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

df[['Close', 'MA20', 'MA50']].head(25)

#Now, let's calculate the Relative Strength Index (RSI) to further assess volatility.

def calculate_rsi(data, window=14):
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# Calculate RSI
df['RSI'] = calculate_rsi(df)

df[['Close', 'RSI']].head(25)
