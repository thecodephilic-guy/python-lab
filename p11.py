# WAP of String slicing in Python to rotate a string

def rotate_string(input_string, rotations):
    rotated_string = input_string[rotations % len(input_string):] + input_string[:rotations % len(input_string)]
    return rotated_string

# Example string
input_string = input("Enter a string: ")

# Number of rotations
rotations = int(input("Enter the number of rotations: "))

# Rotate the string
rotated_string = rotate_string(input_string, rotations)

# Output the rotated string
print("Rotated string:", rotated_string)
