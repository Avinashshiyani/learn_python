# 2
# Load the dataset (student_marks.csv) into a pandas DataFrame.
# Display information: number of columns, number of rows/records and the name of all
# columns
import pandas as pd

# Load the dataset
df = pd.read_csv('student_marks.csv')

# Display basic info
print("Number of columns:", df.shape[1])
print("Number of rows:", df.shape[0])
print("Column names:", df.columns.tolist())