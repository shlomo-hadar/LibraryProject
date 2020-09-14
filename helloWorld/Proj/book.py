##################
class Book:
    def __init__(self, title="", author="", publication_year=0, comic=0,
                 dramatic=0, educational=0, hosting_library="", current_holder=""):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.comic = comic
        self.dramatic = dramatic
        self.educational = educational
        self.current_holder = current_holder
        self.hosting_library = hosting_library

    def __str__(self):
        """
        prints out the book information
        :return: the string representation of the book
        """
        return ("[" + self.title + ", " + self.author + ", " + str(self.publication_year) +
                ", " + str(self.comic) + ", " + str(self.dramatic) + ", " + str(self.educational) + "]")
