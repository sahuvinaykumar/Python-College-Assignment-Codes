import math

# Get number of elements
n = int(input("Enter the number of elements: "))

# Initialize product to 1
product = 1

# Loop to read and multiply elements
for _ in range(n):
    num = float(input("Enter an element: "))
    product *= num

# Calculate geometric mean
geometric_mean = math.pow(product, 1/n)

# Print the geometric mean
print(f"Geometric mean: {geometric_mean:.4f}")