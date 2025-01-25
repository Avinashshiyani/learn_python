# Line Chart: English marks for first 10 students
df.sort_values(by='Rollno', inplace=True)
plt.plot(df['Rollno'][:10], df['English'][:10], marker='o', color='red')
plt.title("Progress of English Marks for First 10 Students")
plt.xlabel("Roll Number")
plt.ylabel("English Marks")
plt.show()