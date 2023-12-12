def countdown(n):
  """
  This function prints the numbers from n to 0 using recursion.

  Args:
    n: The starting number.
  """
  if n > 0:
    print(n)
    countdown(n - 1)

# Get the starting number from the user
n = int(input("Enter a number: "))

# Start the countdown
countdown(n)