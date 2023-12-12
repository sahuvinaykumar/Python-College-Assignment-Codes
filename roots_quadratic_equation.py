import math

def quadratic_formula(a, b, c):
  """
  This function calculates the roots of a quadratic equation.

  Args:
      a: The coefficient of the x^2 term.
      b: The coefficient of the x term.
      c: The constant term.

  Returns:
      A tuple containing the two roots of the equation.
  """
  discriminant = b**2 - 4 * a * c

  if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2
  elif discriminant == 0:
    root = -b / (2 * a)
    return root, root
  else:
    return None, None

# Get the coefficients from the user
a = float(input("Enter the coefficient of the x^2 term: "))
b = float(input("Enter the coefficient of the x term: "))
c = float(input("Enter the constant term: "))

# Find the roots
root1, root2 = quadratic_formula(a, b, c)

# Print the results
if root1 is not None and root2 is not None:
  print(f"The roots of the equation are: {root1:.2f} and {root2:.2f}")
elif root1 is not None and root2 is None:
  print(f"The equation has a double root of: {root1:.2f}")
else:
  print("The equation has no real roots.")