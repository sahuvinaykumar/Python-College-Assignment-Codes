def sum_of_digits(number):
  """
  This function calculates the sum of digits of an integer using a while loop.

  Args:
      number: The integer whose sum of digits is to be calculated.

  Returns:
      The sum of digits of the integer.
  """
  sum_of_digits = 0
  while number > 0:
    # Extract the last digit using modulo operator
    last_digit = number % 10

    # Add the last digit to the sum
    sum_of_digits += last_digit

    # Divide the number by 10 to remove the last digit
    number //= 10

  return sum_of_digits

# Get the number from the user
number = int(input("Enter a number: "))

# Calculate the sum of digits
sum_of_digits = sum_of_digits(number)

# Print the sum of digits
print(f"The sum of digits of {number} is: {sum_of_digits}")