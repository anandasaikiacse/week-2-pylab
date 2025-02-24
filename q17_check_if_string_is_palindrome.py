def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]  # Check if the string is equal to its reverse

# User input
string = input("Enter a string to check if it is a palindrome: ")

if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')