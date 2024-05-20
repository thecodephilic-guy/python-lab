# WAP to Counting the frequencies in a list using dictionary in Python

def count_frequencies(lst):
    """Count the frequencies of elements in the given list."""
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

# Example list
example_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 1, 2, 3, 4, 5, 5]

# Counting frequencies
frequencies = count_frequencies(example_list)

# Print the result
print("Frequencies of elements in the list:")
for key, value in frequencies.items():
    print(f"{key}: {value}")
