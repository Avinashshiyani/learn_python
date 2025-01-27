# Pie Chart: Distribution by Category
category_counts = df['Category'].value_counts()
print(category_counts)
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
plt.title("Distribution of Students by Category")
plt.show()