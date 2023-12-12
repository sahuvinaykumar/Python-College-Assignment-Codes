# Define the integer
number = 12345

# Initialize an empty string to store the reversed number
reversed_number = ""

# Loop until the number becomes zero
while number > 0:
    # Extract the last digit using modulo operator
    last_digit = number % 10

    # Add the last digit to the reversed number string
    reversed_number += str(last_digit)

    # Divide the number by 10 to remove the last digit
    number //= 10

# Convert the reversed number string to an integer
reversed_number = int(reversed_number)

# Print the reversed number
print(f"The reversed number is: {reversed_number}")