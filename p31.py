# WAP to Dictionary to find mirror characters in a string 

def find_mirror_characters(input_string):
    # Define the mirror mapping dictionary
    mirror_mapping = {
        'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
        'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k',
        'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
        'y': 'b', 'z': 'a'
    }
    
    # Initialize the result string
    mirrored_string = ""
    
    # Convert each character in the input string to its mirror character
    for char in input_string:
        # Convert to lowercase to handle both uppercase and lowercase letters
        lower_char = char.lower()
        
        # Find the mirror character if it exists
        if lower_char in mirror_mapping:
            mirror_char = mirror_mapping[lower_char]
            
            # Preserve the original case
            if char.isupper():
                mirror_char = mirror_char.upper()
            
            mirrored_string += mirror_char
        else:
            mirrored_string += char
    
    return mirrored_string

# Test the function
input_string = "HelloWorld"
mirrored_output = find_mirror_characters(input_string)
print("Original string:", input_string)
print("Mirrored string:", mirrored_output)
