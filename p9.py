# WAP to Break a list into chunks of size N in Python

def chunk_list(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

# Taking user input for the list of elements
input_str = input("Enter elements separated by spaces: ")
elements = input_str.split()

# Converting elements to integers (optional)
elements = list(map(int, elements))

# Taking user input for the chunk size
chunk_size = int(input("Enter the chunk size: "))

# Breaking the list into chunks
chunks = chunk_list(elements, chunk_size)

# Output the list of chunks
print("List broken into chunks of size", chunk_size, ":", chunks)
