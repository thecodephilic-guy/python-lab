# WAP to Sort a list of tuples by second Item

def sort_by_second_item(tuples_list):
    """Sort a list of tuples by the second item in each tuple."""
    return sorted(tuples_list, key=lambda x: x[1])

# Example list of tuples
tuples_list = [('a', 3), ('b', 1), ('c', 2), ('d', 4)]

# Sort the list by the second item
sorted_list = sort_by_second_item(tuples_list)

# Print the result
print("Sorted list of tuples by second item:")
for t in sorted_list:
    print(t)
