# Create a function named create palindrome. It should take a string, create a palindrome from it and then return it.

def palindrom(text):
    text = text + text[::-1]
    return text

print(palindrom("Bence"))
