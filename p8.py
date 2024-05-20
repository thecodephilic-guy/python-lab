# WAP to find Cumulative sum of a list 


def cumulative_sum(numbers):
    cum_sum = []
    total = 0
    for num in numbers:
        total += num
        cum_sum.append(total)
    return cum_sum

# Taking user input for the list of numbers
input_str = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_str.split()))

# Find cumulative sum
cumulative_result = cumulative_sum(numbers)

# Output the cumulative sum
print("Cumulative sum of the list:", cumulative_result)
