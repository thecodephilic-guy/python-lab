# WAP to Convert a list of Tuples into Dictionary 

def tuples_to_dict(tuples_list):
    """Convert a list of tuples into a dictionary using the dict constructor."""
    return dict(tuples_list)

# Example list of tuples
tuples_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# Convert to dictionary
result_dict = tuples_to_dict(tuples_list)

# Print the result
print("Dictionary:", result_dict)
