example = "In a dishwasher far far away";

# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away


example[4:16].append = "galaxy"



# for n in example range([:4], [16:]):
#     n.append = "galaxy"
print(example)
