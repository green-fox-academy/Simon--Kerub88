# Create a sum method in your class which has a list of integers as parameter
# It should return the sum of the elements in the list
# Follow these steps:
#     Add a new test case
#     Instantiate your class
#     create a list of integers
#     use the assertEquals to test the result of the created sum method
# Run it
# Create different tests where you
#     test your method with an empyt list
#     with a list with one element in it
#     with multiple elements in it
#     with a null
# Run them
# Fix your code if needed

class NewClass:

    list_of_integers = [3, 1, 6, 5, 9, 2]

    def sum(self):
        print(sum(self))


stuff = NewClass()
stuff = [3, 1, 6, 5, 9, 2]
stuff.sum()
