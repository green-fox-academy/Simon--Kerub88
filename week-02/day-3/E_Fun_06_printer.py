# - Create a function called `printer`
#   which prints the input parameters
#   (can have multiple number of arguments)

def printer(*stuff_to_drop):
    for p in range(0, len(stuff_to_drop)):
        print(stuff_to_drop[p], end = " ")

printer(input("Enter stuff: "))
