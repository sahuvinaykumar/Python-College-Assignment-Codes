def is_prime(number):
  """
  This function checks if a number is prime.

  Args:
      number: The number to be checked.

  Returns:
      True if the number is prime, False otherwise.
  """
  if number <= 1:
    return False
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      return False
  return True

# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")