# WAP Program to find sum of aray

def arraySum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = [1, 2, 3, 4, 5]
print("Sum of array is:", arraySum(arr))