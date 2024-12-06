# 13
# Calculate the total marks for each student and add it as a new column as total. Display
# updated DataFrame

df['Total'] = df[['Maths', 'English', 'Science']].sum(axis=1)

# Displaying the updated DataFrame
print(df)