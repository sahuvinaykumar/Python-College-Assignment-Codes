def matrix_addition(matrix1, matrix2):
  """
  This function adds two matrices.

  Args:
      matrix1: The first matrix.
      matrix2: The second matrix.

  Returns:
      The sum of the two matrices.
  """
  # Check if the matrices have compatible dimensions
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    raise ValueError("Matrices must have the same dimensions.")

  # Initialize the result matrix
  result_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

  # Add corresponding elements of each matrix
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

  return result_matrix

# Sample matrices
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]

# Add the matrices
result_matrix = matrix_addition(matrix1, matrix2)

# Print the result
print("Matrix A:")
print(matrix1)
print("\nMatrix B:")
print(matrix2)
print("\nSum of matrices:")
print(result_matrix)