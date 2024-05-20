# WAP to find the largest element in an array

def find_largest(arr):
        if len(arr) == 0:
            return None
        
        largest = arr[0]
        for i in arr:
            if i > largest:
                largest = i
        return largest


arr = [3, 2, 34, 5, 23]
largest = find_largest(arr)
print("List is empty" if largest == None else "Largest element in array is:", largest)