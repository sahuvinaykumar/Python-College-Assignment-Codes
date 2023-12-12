def is_leap_year(year):
  """
  This function checks if a year is a leap year.

  Args:
      year: The year to be checked.

  Returns:
      True if the year is a leap year, False otherwise.
  """
  if year % 4 != 0:
    return False
  elif year % 100 == 0 and year % 400 != 0:
    return False
  else:
    return True

# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")