import numpy as np

vector = np.random.uniform(1, 20, size=20)

matrix = vector.reshape(4, 5)

print("Original Matrix:")
print(matrix)

max_indices = np.argmax(matrix, axis=1)

rows = np.arange(matrix.shape[0])
matrix[rows, max_indices] = 0

print("\nModified Matrix:")
print(matrix)
