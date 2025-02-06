# 7-14. Matrix statistics
print("Minimum values (row-wise):", np.min(matrix, axis=1))
print("Maximum values (column-wise):", np.max(matrix, axis=0))
print("Maximum value in matrix:", np.max(matrix))
print("Minimum value in matrix:", np.min(matrix))
print("Mean of matrix:", np.mean(matrix))
print("Median of matrix:", np.median(matrix))
print("Variance of matrix:", np.var(matrix))
print("Standard deviation of matrix:", np.std(matrix))