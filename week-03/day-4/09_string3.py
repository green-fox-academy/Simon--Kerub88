# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

string_list = "triple xxx and triple yyy"

def letter_changer(s):
    if s == "":
        return s
    else:
        return s[0] + "*" + letter_changer(s[1:])

print(letter_changer(string_list))
