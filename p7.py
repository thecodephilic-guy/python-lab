# WAP print duplicates from a list of integers.

def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Taking user input for the list of integers
input_str = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_str.split()))

# Find duplicates
duplicate_numbers = find_duplicates(numbers)

# Output the duplicates
if duplicate_numbers:
    print("Duplicates in the list:", duplicate_numbers)
else:
    print("No duplicates found in the list.")
