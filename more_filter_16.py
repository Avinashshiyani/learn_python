# 16
# Find the student with the highest total marks and display their name.
# Find the student with the lowest total marks and display their name. 
import pandas as pd

import pandas as pd

# Load the DataFrame from the CSV
df = pd.read_csv("student_marks.csv")

# Calculate total marks by summing up 'English', 'Maths', and 'Science' columns
df['Total'] = df[['English', 'Maths', 'Science']].sum(axis=1)

top_student = df.loc[df['Total'].idxmax()]
print(f"Top student is {top_student['Name']} with total marks: {top_student['Total']}")


low_student = df.loc[df['Total'].idxmin()]
print(f"Lowest scoring student is {low_student['Name']} with total marks: {low_student['Total']}")

