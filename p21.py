# WAP to read an entire text file

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "The specified file was not found."

file_path = "file.txt"
# Read the entire file
file_content = read_file(file_path)

# Print the content of the file
print("Content of the file:")
print(file_content)
