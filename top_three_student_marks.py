# 20
# Find and display the rows of the top 3 students with the highest total marks.
import pandas as pd

# Load the DataFrame from the CSV
df = pd.read_csv("student_marks.csv")

# Calculate total marks by summing up 'English', 'Maths', and 'Science' columns
df['Total'] = df[['English', 'Maths', 'Science']].sum(axis=1)

# Find the top 3 students with the highest total marks
top_students = df.nlargest(3, 'Total')

# Display the rows of the top 3 students
print(top_students)
