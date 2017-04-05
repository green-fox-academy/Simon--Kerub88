# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
# Create a test for that.
inp1 = "tokyo"
inp2 = "kyoto"


def anagram(input1, input2):
    if len(input1) == len(input2):
        for i in input1:
            for t in input2:
                if input1[i] = input1[t]:
                    print("yeah")

anagram(inp1, inp2)
