# 6 . Display student rows with category ‘B’ or ‘C’.
filtered_students = df[df['Category'].isin(['B', 'C'])]

print(filtered_students)