# 17
# Find the student name with the maximum marks in each subject.
import pandas as pd

# Load the DataFrame from the CSV
df = pd.read_csv("student_marks.csv")

# Find the student with the highest marks in English
top_english_student = df.loc[df['English'].idxmax()]
print(f"Top student in English is {top_english_student['Name']} with {top_english_student['English']} marks")

# Find the student with the highest marks in Maths
top_maths_student = df.loc[df['Maths'].idxmax()]
print(f"Top student in Maths is {top_maths_student['Name']} with {top_maths_student['Maths']} marks")

# Find the student with the highest marks in Science
top_science_student = df.loc[df['Science'].idxmax()]
print(f"Top student in Science is {top_science_student['Name']} with {top_science_student['Science']} marks")