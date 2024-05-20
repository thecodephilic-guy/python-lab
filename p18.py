# WAP to remove all duplicates words from a given sentence 

def remove_duplicate_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Use an ordered set to keep track of unique words while preserving order
    unique_words = []
    seen = set()
    
    for word in words:
        if word.lower() not in seen:
            unique_words.append(word)
            seen.add(word.lower())  # Use lower() to make the operation case-insensitive
    
    # Join the unique words back into a sentence
    return ' '.join(unique_words)

# Example sentence
sentence = input("Enter your sentence: ")

# Remove duplicate words
result = remove_duplicate_words(sentence)

# Output the result
print("Sentence after removing duplicate words:", result)
