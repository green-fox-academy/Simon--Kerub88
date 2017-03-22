# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

# def printer(stuff_to_drop):
#     print(stuff_to_drop)
#
# printer("Faradt vagyok")


def printer(*args):
    for i in range(0, len(args)):
        print(args[i], end=" ")

printer(input("Enter words: "))
