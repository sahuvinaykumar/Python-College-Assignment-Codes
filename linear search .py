def linear_search(list1, n, key):
  """
  This function performs linear search on a list.

  Args:
    list1: The list to search.
    n: The number of elements in the list.
    key: The element to search for.

  Returns:
    The index of the element if found, -1 otherwise.
  """
  for i in range(0, n):
    if list1[i] == key:
      return i
  return -1

# Get the list from the user
list1 = [int(x) for x in input("Enter the list elements separated by space: ").split()]

# Get the key from the user
key = int(input("Enter the element to search for: "))

# Find the index of the key
index = linear_search(list1, len(list1), key)

# Print the result
if index == -1:
  print(f"Element {key} not found in the list.")
else:
  print(f"Element {key} found at index {index}.")