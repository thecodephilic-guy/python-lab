# (b) WAP to access if a file is closed or not

def check_file_closed(file_path):
    try:
        file = open(file_path, 'r')
        print(f"Is the file '{file_path}' closed? {file.closed}")
        file.close()
        print(f"Is the file '{file_path}' closed after closing? {file.closed}")
    except FileNotFoundError:
        print("The specified file was not found.")

# File path
file_path = 'input.txt'

# Check if the file is closed or not
check_file_closed(file_path)
