# WAP to raise a custom exception that could be raised 
# when the text entered by a user consist of less than 3 characters.

class TextTooShortError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"Error: Text '{self.text}' consists of less than 3 characters."

def check_text_length(text):
    if len(text) < 3:
        raise TextTooShortError(text)
    else:
        print("Text is valid.")

# Test cases
try:
    check_text_length("ab")  # Raises TextTooShortError
except TextTooShortError as e:
    print(e)  # Output: Error: Text 'ab' consists of less than 3 characters.

try:
    check_text_length("abc")  # Text is valid
except TextTooShortError as e:
    print(e)
