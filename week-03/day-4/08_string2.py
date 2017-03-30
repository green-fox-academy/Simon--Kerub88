# Given a string, compute recursively a new string where all the 'x' chars have been removed.


string_list = "triple xxx and triple yyy"


# print(string_list[1+1])

def letter_changer(s):
    if s == "":
        return s
    elif s[0] == "x":
        return " " + (letter_changer(s[1:]))
    else:
        return s[0] + letter_changer(s[1:])

print(letter_changer(string_list))
