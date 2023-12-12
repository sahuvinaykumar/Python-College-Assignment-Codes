# Get the number of elements
n = int(input("Enter the number of elements: "))

# Initialize an empty list
numbers = []

# Get the elements from the user
for _ in range(n):
  num = float(input("Enter an element: "))
  numbers.append(num)

# Calculate the sum using the sum() function
sum_of_numbers = sum(numbers)

# Print the sum
print(f"The sum of the elements is: {sum_of_numbers}")