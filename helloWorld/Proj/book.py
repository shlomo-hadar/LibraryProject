##################
class Book:
    def __init__(self, title="", author="", publication_year=0, comic=0,
                 dramatic=0, educational=0, hosting_library="", current_borrower=""):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.comic = comic
        self.dramatic = dramatic
        self.educational = educational
        self.current_borrower = current_borrower
        self.hosting_library = hosting_library

    def print_book_info(self):
        #  prints out the book information
        print("book Title:", self.title, "\n\tauthor:", self.author, "\n\tPublicationYear:", str(self.publication_year),
              "\n\tComic:", str(self.comic), "\n\tDramatic:", str(self.dramatic), "\n\tEducational:", str(self.educational) + "\n")
