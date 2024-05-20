# WAP to merge two dictionaries

def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of dict1
    merged_dict.update(dict2)  # Update with the key-value pairs from dict2
    return merged_dict

# Example dictionaries
dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'email': 'alice@example.com'}

# Merge the dictionaries
merged_dict = merge_dictionaries(dict1, dict2)

# Output the merged dictionary
print("Merged dictionary:", merged_dict)
