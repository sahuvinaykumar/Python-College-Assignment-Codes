def binary_search(list1, low, high, key):
  """
  This function performs binary search on a list.

  Args:
    list1: The sorted list to search.
    low: The lower bound of the search range.
    high: The upper bound of the search range.
    key: The element to search for.

  Returns:
    The index of the element if found, -1 otherwise.
  """
  if low > high:
    return -1
  mid = (low + high) // 2

  if list1[mid] == key:
    return mid
  elif list1[mid] < key:
    return binary_search(list1, mid + 1, high, key)
  else:
    return binary_search(list1, low, mid - 1, key)

# Get the sorted list from the user
list1 = [int(x) for x in input("Enter the sorted list elements separated by space: ").split()]

# Get the key from the user
key = int(input("Enter the element to search for: "))

# Find the index of the key
index = binary_search(list1, 0, len(list1) - 1, key)

# Print the result
if index == -1:
  print(f"Element {key} not found in the list.")
else:
  print(f"Element {key} found at index {index}.")