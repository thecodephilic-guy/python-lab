# WAP to Find common elements in three sorted arrays by dictionary intersection 

def find_common_elements(arr1, arr2, arr3):
    # Convert each array to a dictionary with elements as keys
    dict1 = {element: True for element in arr1}
    dict2 = {element: True for element in arr2}
    dict3 = {element: True for element in arr3}

    # Find the intersection of the three dictionaries
    common_elements = dict1.keys() & dict2.keys() & dict3.keys()
    
    return list(common_elements)

# Example sorted arrays
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
arr3 = [2, 5, 6, 8]

# Find common elements
common_elements = find_common_elements(arr1, arr2, arr3)

# Output the common elements
print("Common elements in the three arrays:", common_elements)
