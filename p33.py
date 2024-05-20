# WAP Scraping And Finding Ordered Words In A Dictionary using Python

def is_ordered(word):
    """Check if the letters of the word are in alphabetical order."""
    return all(word[i] <= word[i + 1] for i in range(len(word) - 1))

def find_ordered_words(words):
    """Return a list of words that have their letters in alphabetical order."""
    return [word for word in words if is_ordered(word)]

# Predefined list of words
words = [
    "abc", "hello", "xyz", "algorithm", "loops", "apple", "ace", "bill"
]

# Find ordered words
ordered_words = find_ordered_words(words)

# Print ordered words
print(f"Ordered words ({len(ordered_words)}):")
for word in ordered_words:
    print(word)
