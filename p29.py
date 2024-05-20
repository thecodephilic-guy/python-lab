# WAP of exception argument
# In Python, you can access the exception argument using the as keyword within the except block

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError as e:
        print("Error:", e)

# Test cases
divide_numbers(10, 2)   # Output: Result of division: 5.0
divide_numbers(10, 0)   # Output: Error: division by zero
