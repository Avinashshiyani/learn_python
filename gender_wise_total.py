# 18
# Display the gender-wise total number of students.
import pandas as pd

# Load the DataFrame from the CSV
df = pd.read_csv("student_marks.csv")

# Group by 'Gender' and count the number of students in each gender
gender_count = df.groupby('Gender').size()

# Display the result
print(gender_count)
