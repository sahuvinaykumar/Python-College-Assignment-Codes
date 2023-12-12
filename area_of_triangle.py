# Define the sides of the triangle
a = 5
b = 7
c = 8

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area of the triangle using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the area of the triangle
print(f"The area of the triangle is: {area:.2f}")