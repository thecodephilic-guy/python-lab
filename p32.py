# WAP to dictionary intersection example (Make a string using deletion and rearrangement)

from collections import Counter

def can_form_string(str1, str2):
    # Create frequency dictionaries for both strings
    count_str1 = Counter(str1)
    count_str2 = Counter(str2)

    # Check if str2 can be formed using the characters of str1
    for char, count in count_str2.items():
        if count_str1[char] < count:
            return False

    return True

# Test cases
str1 = "helloworld"
str2 = "hello"

if can_form_string(str1, str2):
    print(f"'{str2}' can be formed from '{str1}' by deletion and rearrangement.")
else:
    print(f"'{str2}' cannot be formed from '{str1}'.")

str1 = "helloworld"
str2 = "worlds"

if can_form_string(str1, str2):
    print(f"'{str2}' can be formed from '{str1}' by deletion and rearrangement.")
else:
    print(f"'{str2}' cannot be formed from '{str1}'.")
