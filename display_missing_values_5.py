# 5
# Display the total number of missing values per column. Fill missing marks with the mean
# of the column/subject. Also handle missing values appropriately if exists in any column.
# 6. Display student rows with category ‘B’ or ‘C’

missing_values_count = df.isnull().sum()
print("Total Missing Values per Column:")
print(missing_values_count)

for column in ['English', 'Maths', 'Science']:
    df[column].fillna(df[column].mean(), inplace=True)

remaining_missing_values = df.isnull().sum()
print("\nMissing Values after filling:")
print(remaining_missing_values)

df.fillna({'Name': 'Unknown', 'Category': 'Unknown'}, inplace=True)

# Final check for any remaining missing values
final_missing_values = df.isnull().sum()
print("\nFinal Missing Values:")
print(final_missing_values)