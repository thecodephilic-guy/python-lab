# WAP to Find all duplicate characters in string

def find_duplicate_characters(input_string):
    duplicates = []
    char_count = {}

    # Count occurrences of each character
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find duplicates
    for char, count in char_count.items():
        if count > 1:
            duplicates.append(char)

    return duplicates

# Example string
input_string = input("Enter a string: ")

# Find duplicate characters
duplicate_characters = find_duplicate_characters(input_string)

# Output the duplicate characters
if duplicate_characters:
    print("Duplicate characters in the string:", duplicate_characters)
else:
    print("No duplicate characters found in the string.")
