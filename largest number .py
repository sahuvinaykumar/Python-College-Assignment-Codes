def find_largest_number(numbers):
  """
  This function finds the largest number in a list without using any built-in functions.

  Args:
      numbers: The list of numbers.

  Returns:
      The largest number in the list.
  """
  largest_number = numbers[0]
  for number in numbers:
    if number > largest_number:
      largest_number = number
  return largest_number

# Sample list of numbers
numbers = [10, 2, 5, 7, 15]

# Find the largest number
largest = find_largest_number(numbers)

# Print the result
print(f"The largest number in the list is: {largest}")