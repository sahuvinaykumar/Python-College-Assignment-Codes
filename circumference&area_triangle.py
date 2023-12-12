# Import math library for pi value
import math

# Get radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate circumference
circumference = 2 * math.pi * radius

# Calculate area
area = math.pi * radius * radius

# Display results
print(f"Circumference of the circle: {circumference:.2f}")
print(f"Area of the circle: {area:.2f}")