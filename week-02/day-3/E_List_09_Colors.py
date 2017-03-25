# - Create a two dimensional list
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`

colors = {"green" : ["lime", "forest green", "olive", "pale green", "spring green"], "red" : ["orange red", "red", "tomato"], "pink" : ["orchid", "violet", "pink", "hot pink"]}


# egy olyan loopot hozok letre ahol ha key elemhez erkezunk akkor menjen vegig a listaelemein es printelje ki a key neve ala a valuekat

for k, v in colors.items():
    # if colors[c] == "green":

    print(k, v)
