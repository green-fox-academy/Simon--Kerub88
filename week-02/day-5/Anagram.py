# Create a function named is anagram following your current language's style guide. It should take two strings and return a boolean value depending on whether its an anagram or not.

def is_anagram(t1,t2):
    if t1[::-1] == t2:
        return True
    else:
        return False


print(is_anagram("dog", "god"))
print(is_anagram("cbaed", "abcde"))
print(is_anagram("green", "fox"))
