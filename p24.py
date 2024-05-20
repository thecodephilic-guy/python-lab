# WAP of function overloading

# using variable-lenght arguments:

def add(*args):
    return sum(args)

# Examples of calling the add function
print(add(1, 2))         # Output: 3
print(add(1, 2, 3))      # Output: 6
print(add())             # Output: 0
print(add(5, 10, 15))    # Output: 30
