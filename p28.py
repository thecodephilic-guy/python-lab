# WAP to check for ZeroDivisonError

def divide_numbers(a, b):
    try:
        result = a / b
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero!")

# Test cases
divide_numbers(10, 2)   # Output: Result of division: 5.0
divide_numbers(10, 0)   # Output: Error: Division by zero!
