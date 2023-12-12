# Loop through the range 100 to 200
for num in range(100, 201):
  # Extract the digits
  first_digit = num // 10
  second_digit = num % 10

  # Calculate the sum of digits
  sum_of_digits = first_digit + second_digit

  # Check if the sum of digits is even
  if sum_of_digits % 2 == 0:
    # Print the number
    print(num)