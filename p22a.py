# (a) WAP to read a file line by line and write it into a list in another file.

def read_and_write_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        with open(output_file, 'w') as outfile:
            outfile.write(str(lines))

    except FileNotFoundError:
        print("The specified input file was not found.")

# File paths
input_file = 'input.txt'
output_file = 'output.txt'

# Read and write lines
read_and_write_lines(input_file, output_file)

# Print confirmation
print(f"Lines from {input_file} have been written to {output_file} as a list.")
