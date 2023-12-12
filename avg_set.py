# Define the set of integers
numbers = [1, 2, 3, 4, 5]

# Initialize a variable to store the sum
total = 0

# Loop through the list and add each element to the sum
for number in numbers:
    total += number

# Calculate the average
average = total / len(numbers)

# Print the average
print(f"The average of the set is: {average}")