# write a function that takes a filename and returns the number of lines the
# file contains. It should return zero if the file does not exist.

def lines_counter(file_name):
    try:
        fr = open(file_name, mode = "r")
        text = fr.readlines()
        return len(text)

    except FileNotFoundError:
        return "zero"

print(lines_counter("zero1.txt"))
