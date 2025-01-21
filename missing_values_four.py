# 3
# Display the total number of missing values per column. Fill missing marks with the mean
# of the column/subject. Also handle missing values appropriately if exists in any column. 
# Display missing values per column
print("Missing values per column:\n", df.isnull().sum())
df['English'] = df['English'].fillna(df['English'].mean())
df['Maths'] = df['Maths'].fillna(df['Maths'].mean())
df['Science'] = df['Science'].fillna(df['Science'].mean())
