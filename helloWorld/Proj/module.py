ID=0
class Library:
    def __init__(self, name = "default", maxNumOfBooks = 100, maxNumOfCustomers = 50,
                 maxNumOfLendedBooks = 2, listOfBooks = [], dictOfNumOfBooks = {}, listOfClients=[]):
        # the information of an independent library
        self.name = name  #library name
        self.numOfBooks = 0  #current number of books that the library is hosting
        self.maxNumOfBooks = maxNumOfBooks  #maximum books that the library can host
        self.numOfCustomers = 0  #current amount of clients
        self.maxNumOfCustomers = maxNumOfCustomers  #maximum amount of clients
        self.maxNumOfLendedBooks = maxNumOfLendedBooks  #maximum books that a client can borrow at the same time
        self.listOfBooks = listOfBooks  #contains a book class obj's
        self.dictOfNumOfBooks = dictOfNumOfBooks  #keeps track of the amount of copies of each individual book
        self.listOfClients = listOfClients  #list of the library clients

    def addBook(self,book):
        #  adds a new book to the library
        if self.numOfBooks != self.maxNumOfBooks:
            self.listOfBooks.append(book)
            if (book.title + " by " + book.author) in self.dictOfNumOfBooks:
                self.dictOfNumOfBooks[book.title + " by " + book.author] += 1
                book.currentHolder = self.name
                book.hostingLibrary = self.name
                self.numOfBooks += 1
            else:
                self.dictOfNumOfBooks[book.title + " by " + book.author] = 1
                book.currentHolder = self.name
                book.hostingLibrary = self.name
                self.numOfBooks += 1
        else:
            print("book addition failed")

    def addClient(self, client):
        #  adding the client to the list of client in the library object
        #  and the library to the list of the client registerd libraries list
        if client not in self.listOfClients:
            self.listOfClients.append(client)
            client.listOfLibrariesRegisteredTo.append(self)

    def printListOfBooks(self):
        #  prints the books of a library with all of their info
        i=1
        listInf = ""
        for book in self.listOfBooks:
            listInf += "book "+str(i) + ": \n\t"+"Title: "+ book.title + "\n\tAuthor: " + book.author + "\n\tYear Of Publication: " \
              + str(book.publicationYear) + "\n\tComic Value: " + str(book.comic) + "\n\tDramatic Value: " + str(book.dramatic) \
                + "\n\tEducational Value: " + str(book.educational)+"\n\n"
            i += 1
        return listInf

##################
class Book:
    def __init__(self, title = "", author = "", publicationYear =0  #adding a book to the lib
                 , comic = 0, dramatic = 0, educational = 0, hostingLibrary = "", currentBorrower = ""):
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
        self.comic = comic
        self.dramatic = dramatic
        self.educational = educational
        self.currentHolder = currentBorrower #will hold firstName+lastName+id
        self.hostingLibrary = hostingLibrary

    def printBookInfo(self):
        #  prints out the book information
        print("book Title:", self.title, "\n\tautor:", self.author, "\n\tPublicationYear:", str(self.publicationYear)
            , "\n\tComic:", str(self.comic), "\n\tDramatic:", str(self.dramatic), "\n\tEducational:", str(self.educational) + "\n")

class Client:

    def __init__(self, firstName = "Shniki", lastName = "Abutbul", comic = 0, dramatic = 0, educational = 0, joiThreshold = 0, listOfLibrariesRegisteredTo=[]):
        self.firstName = firstName
        self.lastName = lastName
        self.id = self.setID()
        self.comic = comic
        self.dramatic = dramatic
        self.educational = educational
        self.joiThreshold = joiThreshold
        self.listOfLibrariesRegisteredTo = listOfLibrariesRegisteredTo
        self.listofBooksInPossetion = []

    def setID(self):
        #  setting the current user id and ascending it for the next customer
        global ID
        ID += 1
        return ID

    def printClientInfo(self):
        #  prints the client information and pushing the id for the next client
        print("first name: " + self.firstName+"\nlast name: "+self.lastName+"\nID: "+str(self.id))

    def borrowBook(self):
        success = 0
        neededBook = input("what book would you like to borrow? ")
        for lib in self.listOfLibrariesRegisteredTo:
            if neededBook in lib.dictOfNumOfBooks:  #checks if the book is in the library
                if (lib.dictOfNumOfBooks[neededBook] > 0):  #checks if the book is in inventory  #####and
                    if self.authenticateLimitOfBooksPossessed(lib):  #checks if the the client can borrow more books from the library
                        lib.dictOfNumOfBooks[neededBook] -= 1
                        for curBook in lib.listOfBooks:
                            if (neededBook == curBook.title+" by " +curBook.author) and curBook.currentHolder == lib.name:
                                curBook.currentHolder = self.firstName+" "+self.lastName
                                self.listofBooksInPossetion.append(curBook)
                                print("the borrow of the book "+curBook.title+ " by " + curBook.author + " was complited successfully\n")
                                success = 1
                                break
                    else:
                        print("you have reached the maximum of books you can borrow at the same time\n")
                else:
                    print("we don't have this book in our inventory.. try again later :)\n")
            if success == 1:
                break
        if success == 0:
            print("the book that you asked for is not in inventory yet")

    def returnBook(self):
        if len(self.listofBooksInPossetion) == 0:
            print("you have not borrowed any books yet\n")
            return
        bookToBeReturned = input("what book would you like to return?")
        bookReturned = 0
        for book in self.listofBooksInPossetion:
            check = book.title + " by " + book.author
            if bookToBeReturned == check:
                book.currentHolder = book.hostingLibrary
                for lib in self.listOfLibrariesRegisteredTo:
                    if book.hostingLibrary == lib.name:
                        lib.dictOfNumOfBooks[bookToBeReturned] += 1
                        del self.listofBooksInPossetion[self.findIndex(check)]
                        bookReturned = 1
                        break
                if bookReturned == 1:
                    print("the book " + book.title + " by " + book.author + " was returned successfully")
                    break
        if bookReturned == 0:
            print("your are not the borrower of the named book")


    def printBooksInPossetion(self):
        #  returns a string whitch contains the info of the books which are currently in the customer hands
        inf=""
        i = 1
        for book in self.listofBooksInPossetion:
            inf += "book" + str(i)+ ":\n\t" + book.title + " by "+ book.author +"\n\t" + "Current Holder: " +book.currentHolder \
                   + "\n\t" + "Hosting Library: " + book.hostingLibrary +"\n\n"
            i += 1
        return inf

    def authenticateLimitOfBooksPossessed(self , lib):
        #  making sure that the number of books that are in the hand of the customer are less than the maximum of books
        #  that could be lended to a certain customer by the library policy
        numOfBooksFromTheLib=0
        for book in self.listofBooksInPossetion:
            if book.hostingLibrary == lib.name:
                numOfBooksFromTheLib += 1
        if numOfBooksFromTheLib < lib.maxNumOfLendedBooks:
            return 1
        return 0

    def authenticateJoiLevel(self, client, book):
        if client.comic*book.client + client.dramatic * book.dramatic + client.educational * book.educational >= client.joiThreshold:
            return 1
        else:
            return 0

    def recommendOnTheBestSuitableBook(self):
        mostSuitable = ["" , 0]
        for lib in self.listOfLibrariesRegisteredTo:
            for book in lib.listOfBooks:
                if (book.comic * self.comic + book.dramatic * self.dramatic + book.educational * self.educational) >= self.joiThreshold \
                        and (book.comic * self.comic + book.dramatic * self.dramatic + book.educational * self.educational) > mostSuitable[1]:
                    mostSuitable[0] = book.title + " by " + book.author
                    mostSuitable[1] = book.comic * self.comic + book.dramatic * self.dramatic + book.educational * self.educational
        print("the recommended book for you is " + mostSuitable[0] + " with a score of: " + str(mostSuitable[1]) + "\n")

    def findIndex(self ,bookToDrop):
        i = 0
        for book in self.listofBooksInPossetion:
            if bookToDrop == book.title + " by " + book.author:
                return i
            i += 1

