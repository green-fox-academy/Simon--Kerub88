# - Create a two dimensional list
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`

# colors = {"green" : ["lime", "forest green", "olive", "pale green", "spring green"], "red" : ["orange red", "red", "tomato"], "pink" : ["orchid", "violet", "pink", "hot pink"]}

# colors_green = {"lime" : "green", "forest green" : "green", "olive" : "green", "pale green" : "green", "spring green" : "green" }
# colors_red = {"orange red" : "red", "red" : "red", "tomato" : "red"}
# colors_pink = {"orchid" : "pink", "violet" : "pink", "pink" : "pink", "hot pink" : "pink"}

# egy olyan loopot hozok letre ahol a valuekat berakja egy listaba es minden listahoz hozzarendeli a kulcsait egy listaba agyazva es a key listakat len-ezem

colors = {"lime" : "green", "forest green" : "green", "olive" : "green", "pale green" : "green", "spring green" : "green", "orange red" : "red", "red" : "red", "tomato" : "red", "orchid" : "pink", "violet" : "pink", "pink" : "pink", "hot pink" : "pink"}

colors_green = []
colors_red = []
colors_pink = []

for k, v in colors.items():
    if v == "green":
        colors_green.append(colors[])
        print
    # if colors[c] == "green":

    print(colors_green)
