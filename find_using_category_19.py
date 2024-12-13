# 19
# Find the number of students in each category (A, B, C) and display the counts for each
# category
import pandas as pd

# Load the DataFrame from the CSV
df = pd.read_csv("student_marks.csv")

# Group by 'Category' and count the number of students in each category
category_count = df.groupby('Category').size()

# Display the result
print(category_count)
