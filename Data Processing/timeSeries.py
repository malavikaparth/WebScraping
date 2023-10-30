import pandas as pd

# Sample time series data (replace this with your dataset)
data = {'date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
        'value': [10, 15, 20, 25, 30]}
df = pd.DataFrame(data)

# Convert the 'date' column to a datetime type and set it as the index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Define the time window for the moving average (e.g., 3 days)
window_size = 3

# Calculate the moving average
moving_average = df['value'].rolling(window=window_size).mean()

# Add the moving average as a new column in the DataFrame
df['moving_average'] = moving_average

print(df)
