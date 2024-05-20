#WAP for Fibonacci numbers

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Input: number of Fibonacci numbers to generate
num = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_numbers = fibonacci(num)

# Output the Fibonacci numbers
print("Fibonacci sequence:")
for number in fib_numbers:
    print(number, end=" ")
