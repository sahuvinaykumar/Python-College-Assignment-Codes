def factorial(n):
  """
  This function calculates the factorial of a number using recursion.

  Args:
      n: The number whose factorial is to be calculated.

  Returns:
      The factorial of the number.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Get the number from the user
number = int(input("Enter a number: "))

# Calculate the factorial
factorial_value = factorial(number)

# Print the factorial
print(f"The factorial of {number} is: {factorial_value}")