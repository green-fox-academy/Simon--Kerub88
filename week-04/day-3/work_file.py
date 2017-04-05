# Create a class, with one method (eg. get_apple()) that returns a string (eg. "apple")
# Create a test for that:
#     Create a test class
#     Create a test method
#     Instantiate an Object from your class in the method
#     Use the assertEquals()
#     The expected parameter should be the same string (eg. "apple")
#     The actual parameter should be the return value of the method (eg. myobject.get_apple())
# Run the test
# Change the expected value to make the test failing
# Run the test
# Fix the returned value to make the test succeeding again

class Apple:

    def __init__(self, eg):
        self.eg = eg

    def get_apple(self):
        return self.eg + "apple"



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


    def sum(self, list1 = []):
        num = 0
        for i in list1:
            num += list1[i]


# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
# Create a test for that.


    def anagram(self, input1, input2):
        if len(input1) == len(input2):
            input1 = list(input1)
            input1.sort()
            input2 = list(input2)
            input2.sort()
            if input2 == input1:
                return True
            else:
                return False
        else:
            return False
