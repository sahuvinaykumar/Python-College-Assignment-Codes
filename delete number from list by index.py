def delete_element(numbers, index):
  """
  This function deletes an element from a list at a specified index.

  Args:
    numbers: The original list.
    index: The index of the element to be deleted.
  """
  del numbers[index]

# Sample list of numbers
numbers = [1, 3, 5, 7, 9]

# Index of the element to be deleted
index = 2

# Delete the element
delete_element(numbers, index)

# Print the modified list
print(f"The list after deletion: {numbers}")