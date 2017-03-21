# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
#
# Surface Area: 600
# Volume: 1000

l = 50
w = 100
h = 30

sa = 2*(l*w+w*h+h*l)
volume = l*w*h
print("Surface Area: ", sa)
print("Volume: ", volume)
