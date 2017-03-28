# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

number = 0

def ten_divider(added_number):
    try:
        result = 10 / added_number
        return result
    except ZeroDivisionError:
        return "fail"

print(ten_divider(number))
