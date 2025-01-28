# Donut Chart: Distribution by Gender
gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', wedgeprops=dict(width=0.3))
plt.title("Distribution of Students by Gender")
plt.show()