# 21-23. Sparse matrix and its details
sparse_matrix = np.array([[0, 0, 3], [0, 2, 0], [1, 0, 0]])
non_zero = np.count_nonzero(sparse_matrix)
total_elements = sparse_matrix.size
zero_elements = total_elements - non_zero
print("Sparse matrix:\n", sparse_matrix)
print("Non-zero values:", non_zero)
print("Zero values:", zero_elements)