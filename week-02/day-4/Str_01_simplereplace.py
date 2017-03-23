example = "In a dishwasher far far away";

# I would like to replace "dishwasher" with "galaxy" in this example
# Please fix it for me!


example = {"1":"In a ", "2":"dishwasher", "3":"far far away" }
example ["2"] = "galaxy "
example = example ["1"] + example ["2"] + example ["3"]
print(example)

# Solution 2

galaxy = "galaxy"
example = example[0:5] + galaxy + example[11:33]

print(example)
