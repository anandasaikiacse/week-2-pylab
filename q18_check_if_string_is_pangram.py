import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)  # Set of all lowercase letters
    s = s.lower()  # Convert string to lowercase
    s = set(s)  # Convert string to a set of characters
    return alphabet.issubset(s)  # Check if all alphabet letters are in the string

# User input
sentence = input("Enter a sentence to check if it is a pangram: ")

if is_pangram(sentence):
    print(f'"{sentence}" is a pangram.')
else:
    print(f'"{sentence}" is not a pangram.')