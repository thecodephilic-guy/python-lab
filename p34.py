# WAP Create a list of tuples from given list having number and its cube in each tuple

def create_tuples_with_cubes(numbers):
    """Create a list of tuples from a list where each tuple contains a number and its cube."""
    return [(num, num**3) for num in numbers]

# Example list of numbers
numbers = [1, 2, 3, 4]

# Create list of tuples
tuples_with_cubes = create_tuples_with_cubes(numbers)

# Print the result
print("List of tuples (number, cube):")
for t in tuples_with_cubes:
    print(t)
