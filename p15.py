# WAP to remove a key from dictionary

def remove_key_from_dict(dictionary, key_to_remove):
    if key_to_remove in dictionary:
        del dictionary[key_to_remove]
        return True
    else:
        return False

# Example dictionary
example_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York',
    'email': 'alice@example.com'
}

# Taking user input for the key to remove
key_to_remove = input("Enter the key to remove: ")

# Attempt to remove the key from the dictionary
key_removed = remove_key_from_dict(example_dict, key_to_remove)

# Output the result
if key_removed:
    print(f"Key '{key_to_remove}' was removed.")
else:
    print(f"Key '{key_to_remove}' not found.")

# Print the updated dictionary
print("Updated dictionary:", example_dict)
