def celsius_to_fahrenheit(celsius):
  """
  This function converts a temperature from degrees Celsius to degrees Fahrenheit.

  Args:
      celsius: The temperature in degrees Celsius.

  Returns:
      The temperature in degrees Fahrenheit.
  """
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

# Get the temperature in Celsius from the user
celsius = float(input("Enter the temperature in degrees Celsius: "))

# Convert the temperature to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print the result
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")