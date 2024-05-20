# WAP to Sort the values of first list using second list

def sort_list_using_second_list(list1, list2):
    zipped_lists = zip(list2, list1)
    sorted_lists = sorted(zipped_lists)
    return [element for _, element in sorted_lists]

# Example lists
list1 = [3, 1, 5, 2, 4]
list2 = [7, 8, 6, 5, 4]

# Sorting list1 using list2
sorted_list1 = sort_list_using_second_list(list1, list2)

# Output the sorted list
print("Sorted list using second list:", sorted_list1)
