class Library:
    def __init__(self, Name = "defalt", MaxNumOfBooks = 100, MaxNumOfCustomers = 50, \
                 MaxNumOfLendedBooks = 2, ListOfBooks = [], DictOfNumOfBooks = {}):
        # the information of an independent library
        self.Name = Name
        self.MaxNumOfBooks = MaxNumOfBooks
        self.MaxNumOfCustomers = MaxNumOfCustomers
        self.MaxNumOfLendedBooks = MaxNumOfLendedBooks
        self.ListOfBooks = ListOfBooks  #contains a book class obj's
        self.DictOfNumOfBooks = DictOfNumOfBooks #keeps track of the amount of copies of each individual book

    def addBook(self,book):##
        #adds a new book to the library
        self.ListOfBooks.append(book)
        if (book.Title + " by " + book.Author) in self.DictOfNumOfBooks:
                self.DictOfNumOfBooks[book.Title + " by " + book.Author] += 1
        else:
            self.DictOfNumOfBooks[book.Title + " by " + book.Author] = 1

    def printListOfBooks(self):#prints the books of a library with all of their info
        i=1
        listInf=""
        for book in self.ListOfBooks:
            listInf += "book "+str(i) + ": \n\t"+"Title: "+ book.Title + "\n\tAuthor: " + book.Author + "\n\tYear Of Publication: " \
              + str(book.PublicationYear) + "\n\tComic Value: " + str(book.Comic) + "\n\tDramatic Value: " + str(book.Dramatic) \
                + "\n\tEducational Value: " + str(book.Educational)+"\n\n"
            i+=1
        return listInf

##################
class Book:
    def __init__(self,Title = "", Author = "", PublicationYear =0 \
                 , Comic = 0, Dramatic = 0, Educational = 0, HostingLibrary = "", CurrentBorrower = ""):
        self.Title = Title
        self.Author = Author
        self.PublicationYear = PublicationYear
        self.Comic = Comic
        self.Dramatic = Dramatic
        self.Educational = Educational
    def bookInfo(self):
        print("book Title:", self.Title, "autor:", self.autor, "PublicationYear:", self.PublicationYear \
            , "Comic:", self.Comic, "Dramatic:", self.Dramatic, "Educational:", self.Educational )