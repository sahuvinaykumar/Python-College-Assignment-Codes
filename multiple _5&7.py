# Define the integer to be checked
number = 35

# Check divisibility by both 5 and 7 using modulo operator
if number % 5 == 0 and number % 7 == 0:
    print(f"{number} is a multiple of both 5 and 7.")
else:
    print(f"{number} is not a multiple of both 5 and 7.")