# Download any one dataset (CSV file) of your choice from the internet and Load that
# dataset into a pandas DataFrame. Display description of the data using dataframe.
# Display number of columns and rows.
# https://www.kaggle.com/datasets

import pandas as pd

# Load the dataset into a DataFrame (update the file path as needed)
file_path = "bussiness.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Display the description of the DataFrame
print(df.describe())

# Display the number of columns and rows
# print(f"Number of columns: {df.shape[1]}")
# print(f"Number of rows: {df.shape[0]}")
