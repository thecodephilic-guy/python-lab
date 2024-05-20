# WAP to String slicing in Python to check if a string can become empty by recursive deletion 

def can_become_empty(string):
    stack = []
    for char in string:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return not stack

# Example string
input_string = input("Enter a string: ")

# Check if string can become empty by recursive deletion
result = can_become_empty(input_string)

# Output the result
if result:
    print("Yes, the string can become empty by recursive deletion.")
else:
    print("No, the string cannot become empty by recursive deletion.")
