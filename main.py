import numpy as np

# Ask the user for the number of elements
num_elements = int(input("Enter the number of elements: "))
# Calculate the matrix dimension as the nearest square root of the number of elements
matrix_size = int(num_elements ** 0.5)
# Determine the number of rows and columns automatically
# If the matrix is square (fully populated), keep its dimension as matrix_size
# Otherwise, the number of rows will be matrix_size, and the number of columns will be matrix_size + 1
if matrix_size ** 2 == num_elements:
    rows = cols = matrix_size
else:
    rows = matrix_size
    cols = matrix_size + 1
# Create a matrix using arange
matrix = np.arange(rows * cols).reshape(rows, cols)
print("Matrix:")
print(matrix)




