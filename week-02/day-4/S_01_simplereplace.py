example = "In a dishwasher far far away";

# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!
# Expected ouput: In a galaxy far far away


# example[4:16].append = "galaxy"



# for n in example range([:4], [16:]):
#     n.append = "galaxy"
# print(example)

example = {"1":"In a ", "2":"dishwasher", "3":"far far away" }
example ["2"] = "galaxy "
example = example ["1"] + example ["2"] + example ["3"]
print(example)
