# 8
# Sort all the students by English marks column
import pandas as pd
df = pd.read_csv("student_marks.csv")
df.sort_values(by=["English"], ascending=True)