# Create a function named is anagram following your current language's style guide. It should take two strings and return a boolean value depending on whether its an anagram or not.


# Csinalok egy loopot ami t1 minden betujet ellenorzi. Aztan egy masikat ami t2 elemeit ellenorzi es vegul egy if_else-et, hogy megegyeznek e az elemei.

# //////////////////////////////////////////////////

# def is_anagram(t1, t2):
#     t2_list = list(t2)
#
#     position1 = 0
#     go_on = True
#
#     while position1 < len(t1) and go_on:
#         position2 = 0
#         stopped = False
#         while position2 < len(t2_list) and not stopped:
#             if t1[position1] == t2_list[position2]:
#                 stopped = True
#             else:
#                 position2 = position2 + 1
#
#         if stopped:
#             t2_list[position2] = None
#         else:
#             go_on = False
#
#         position1 = position2 +1
#
#     return go_on
#
# print(is_anagram("god", "dog"))
# print(is_anagram("green", "fox"))
# print(is_anagram("abcd", "bcad"))

def anagram(input_1, input_2):
    string = ""
    if len(input_2) == len(input_1):
        for j in input_2:
           if j in input_1:
               string += j
    if string == input_2:
        print(True)

    else:
        print(False)

anagram(str(input("Input a word here: ")),str(input("Input another word here: ")))
