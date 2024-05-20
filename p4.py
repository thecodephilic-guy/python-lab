# WAP to count positive and negative numbers in a list:

def count_positive_negative(num):
    positive = 0
    negative = 0
    for i in num:
        if i>0:
            positive += 1
        else:
            negative += 1

    return positive, negative

num = [2,4,-3, 23, -32]
positive_count, negative_count = count_positive_negative(num)

print("Number of positive numbers: ", positive_count)
print("Number of negative numbers: ", negative_count)
