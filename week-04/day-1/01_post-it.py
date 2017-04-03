# - Create a PostIt class that has
    # a backgroundColor
    # a text on it
    # a textColor
# - Create a few example post-it objects:
    # an orange with blue text: "Idea 1"
    # a pink with black text: "Awesome"
    # a yellow with green text: "Superb!"

class PostIt:

    def __init__(self, backgroundColor, text, textColor):
        self.backgroundColor = backgroundColor
        self.text = text
        self.textColor = textColor

post_it1 = PostIt("orange", "Idea 1", "blue")
post_it2 = PostIt("pink", "Awesome", "black")
post_it3 = PostIt("yellow", "Superb!", "green")

print(post_it1.backgroundColor)
