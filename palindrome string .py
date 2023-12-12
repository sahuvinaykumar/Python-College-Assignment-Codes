def is_palindrome(text):
  """
  This function checks whether a string is a palindrome.

  Args:
      text: The string to be checked.

  Returns:
      True if the string is a palindrome, False otherwise.
  """
  # Convert the string to lowercase and remove spaces
  text = text.lower().replace(" ", "")

  # Check if the string is the same as its reversed version
  return text == text[::-1]

# Sample text
text = "madam"

# Check if the text is a palindrome
if is_palindrome(text):
  print(f"'{text}' is a palindrome.")
else:
  print(f"'{text}' is not a palindrome.")