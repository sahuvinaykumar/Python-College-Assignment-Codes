def generate_primes(n):
  """
  This function generates prime numbers from 1 to n.

  Args:
      n: The upper limit.

  Yields:
      The next prime number in the range.
  """
  # Skip non-positive integers
  if n <= 1:
    return

  # Check for 2 as the first prime
  if n >= 2:
    yield 2

  # Loop for odd numbers only (potential primes)
  for num in range(3, n + 1, 2):
    is_prime = True
    # Check for divisibility by smaller primes
    for i in range(3, int(num**0.5) + 1, 2):
      if num % i == 0:
        is_prime = False
        break
    # If no divisors found, yield the prime number
    if is_prime:
      yield num

# Get the upper limit from the user
n = int(input("Enter the upper limit: "))

# Generate and print prime numbers
print(f"Prime numbers from 1 to {n}:")
for prime in generate_primes(n):
  print(prime)