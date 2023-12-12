def matrix_multiplication(matrix1, matrix2):
  """
  This function multiplies two matrices.

  Args:
      matrix1: The first matrix (m x n).
      matrix2: The second matrix (n x p).

  Returns:
      The product of the two matrices.
  """
  # Check if compatible dimensions
  if len(matrix1[0]) != len(matrix2):
    raise ValueError("Matrix dimensions must be compatible for multiplication.")

  # Initialize the result matrix
  result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

  # Perform multiplication using nested loops
  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      for k in range(len(matrix2)):
        result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

  return result_matrix

# Sample matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Multiply the matrices
result_matrix = matrix_multiplication(matrix1, matrix2)

# Print the result
print("Matrix A:")
print(matrix1)
print("\nMatrix B:")
print(matrix2)
print("\nProduct of matrices:")
print(result_matrix)