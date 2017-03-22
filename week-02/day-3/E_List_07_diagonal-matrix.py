# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output



matrix = [[0 for y in range(4)] for x in range(4)]
for x in range(0, 4):
    row = []

    for y in range(4):
        row.append(0)
    matrix.append(row)
