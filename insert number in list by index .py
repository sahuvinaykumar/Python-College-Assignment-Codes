def insert_number(numbers, position, new_number):
  """
  This function inserts a new number into a list at a specified position.

  Args:
    numbers: The original list.
    position: The position where the new number should be inserted.
    new_number: The number to be inserted.
  """
  numbers.insert(position, new_number)

# Sample list of numbers
numbers = [1, 3, 5, 7]

# Position to insert the new number
position = 2

# New number to be inserted
new_number = 4

# Insert the number
insert_number(numbers, position, new_number)

# Print the modified list
print(f"The list after insertion: {numbers}")