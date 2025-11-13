import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
diagonal = np.diag(matrix)
diagonal_sum = diagonal.sum()

print("Matrix:\n", matrix)
print("Diagonal:", diagonal)
print("Sum of diagonal:", diagonal_sum)
