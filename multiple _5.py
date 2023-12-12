def is_multiple_of_5(number):
    """
    This function checks if a number is a multiple of 5.

    Args:
        number: The number to be checked.

    Returns:
        True if the number is a multiple of 5, False otherwise.
    """
    return number & 1 == 0

# Get the number from the user
number = int(input("Enter a number: "))

# Check if the number is a multiple of 5
if is_multiple_of_5(number):
    print(f"{number} is a multiple of 5.")
else:
    print(f"{number} is not a multiple of 5.")