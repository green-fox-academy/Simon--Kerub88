# - Create an array variable named `ag`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array

ag = [3, 4, 5, 6, 7]

for n in range(0, len(ag)):
    ag[n] *= 2

    print(ag[n])
