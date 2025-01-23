# Bar Graph for average marks by category
avg_marks = df.groupby('Category')[['English', 'Maths', 'Science']].mean()
avg_marks.plot(kind='bar', color=['green', 'gray', 'orange'])
plt.title("Average Marks by Category")
plt.xlabel("Category")
plt.ylabel("Average Marks")
plt.show()