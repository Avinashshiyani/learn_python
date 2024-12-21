# 21
# Save a new csv file with name “student_mark_updated.csv” to store updated DataFrame.
# Verify whether the new CSV file is created or not
import pandas as pd
import os

# Load the DataFrame from the CSV
df = pd.read_csv("student_marks.csv")

# Calculate total marks by summing up 'English', 'Maths', and 'Science' columns
df['Total'] = df[['English', 'Maths', 'Science']].sum(axis=1)

# Save the updated DataFrame to a new CSV file
new_file_name = "student_mark_updated.csv"
df.to_csv(new_file_name, index=False)

# Verify if the new CSV file is created
if os.path.exists(new_file_name):
    print(f"The file '{new_file_name}' has been created successfully.")
else:
    print(f"Failed to create the file '{new_file_name}'.")
