# WAP Remove empty tuples from a list 

def remove_empty_tuples(tuples_list):
    return [t for t in tuples_list if t]

# Taking user input for the list of tuples
input_str = input("Enter tuples separated by commas (use empty parentheses for empty tuples): ")
tuples_list = eval(input_str)  # Evaluate the input string to convert it to a list of tuples

# Remove empty tuples
cleaned_list = remove_empty_tuples(tuples_list)

# Output the list after removing empty tuples
print("List after removing empty tuples:", cleaned_list)