import matplotlib.pyplot as plt
plt.hist(df['English'], bins=10, color='skyblue')
plt.title("Distribution of English Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()