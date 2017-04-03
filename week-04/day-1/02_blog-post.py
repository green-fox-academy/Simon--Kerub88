# BlogPost
#
# - Create a BlogPost class that has
#         an authorName
#         a title
#         a text
#         a publicationDate
# - Create a few blog post objects:
#     "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
#         Lorem ipsum dolor sit amet.
#     "Wait but why" titled by Tim Urban posted at "2010.10.10."
#         A popular long-form, stick-figure-illustrated blog about almost everything.
#     "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
#         Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.

class BlogPost:

    def __init__(self, authorName, title, text, publicationDate):
        self.authorName = authorName
        self.title = title
        self.text = text
        self.publicationDate = publicationDate


blog1 = BlogPost("John Doe", "Lorem Ipsum", "Lorem ipsum dolor sit amet.", "2000.05.04")

print(blog1)