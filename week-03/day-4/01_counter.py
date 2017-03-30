
# Write a recursive function that takes one parameter: n and counts down from n.


def recursive(number):
    if number < 1:
        return 0
    else:
        # print(number)
        return recursive(number - 1), number

print(recursive(7))
