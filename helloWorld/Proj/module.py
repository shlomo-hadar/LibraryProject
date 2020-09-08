ID=0
class Library:
    def __init__(self, name = "defalt", maxNumOfBooks = 100, maxNumOfCustomers = 50,
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
        #adds a new book to the library
        if self.numOfBooks != self.maxNumOfBooks:
            self.listOfBooks.append(book)
            if (book.title + " by " + book.Author) in self.dictOfNumOfBooks:
                self.dictOfNumOfBooks[book.title + " by " + book.author] += 1
                book.currentHolder = self.name
                book.hostingLibrary = self.name
                self.numOfBooks += 1
            else:
                self.dictOfNumOfBooks[book.Title + " by " + book.Author] = 1
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
        #prints the books of a library with all of their info
        i=1
        listInf=""
        for book in self.listOfBooks:
            listInf += "book "+str(i) + ": \n\t"+"Title: "+ book.title + "\n\tAuthor: " + book.author + "\n\tYear Of Publication: " \
              + str(book.publicationYear) + "\n\tComic Value: " + str(book.comic) + "\n\tDramatic Value: " + str(book.dramatic) \
                + "\n\tEducational Value: " + str(book.Educational)+"\n\n"
            i+=1
        return listInf

##################
class Book:
    def __init__(self,title = "", author = "", publicationYear =0
                 , comic = 0, dramatic = 0, educational = 0, hostingLibrary = "", currentBorrower = ""):
        self.title = title
        self.author = author
        self.publicationYear = publicationYear
        self.comic = comic
        self.dramatic = dramatic
        self.educational = educational
        self.currentHolder = "" #will hold firstName+lastName+id
        self.hostingLibrary = ""

    def bookInfo(self):
        #prints out the book information
        print("book Title:", self.title, "autor:", self.author, "PublicationYear:", self.publicationYear
            , "Comic:", self.comic, "Dramatic:", self.dramatic, "Educational:", self.educational )

class Client:

    def __init__(self, firstName = "def", lastName = "def", comic = 0, dramatic = 0, educational = 0, joiThreshold = 0, listOfLibrariesRegisteredTo=[]):
        self.firstName = firstName
        self.lastName = lastName
        self.id = self.setID()
        self.comic = comic
        self.dramatic = dramatic
        self.educational = educational
        self.joiThreshold = joiThreshold
        self.listOfLibrariesRegisteredTo = listOfLibrariesRegisteredTo

    def setID(self):
        #setting the current user id and
        global ID
        ID+=1
        return ID

    def printClientInfo(self):
        #prints the client information and pushing the id for the next client
        print("first name: " + self.firstName+"\nlast name: "+self.lastName+"\nID: "+str(self.id))


