from Proj.module import *


library = Library("Shin Bet",6,75,2)
book = Book("the red lotus","van dam",1974,5,5,5)   #the red lotus by van dam
book2 = Book("the red lotus2","van dam",1977,5,5,5)
book3 = Book("the red lotus3","van dam",1984,5,5,5)
library.addBook(book)
library.addBook(book2)
library.addBook(book3)
library.removeBookFromLibrary()
print(library.printListOfBooks())
book.printBookInfo()
client = Client("abb","lin",2,4,1,15,[])
library.addClient(client)
client.recommendOnTheBestSuitableBook()
client.borrowBook()
client.returnBook()

print(client.printBooksInPossetion())
#print(len(client.booksInPossetion))

""""
print(library.dictOfNumOfBooks)
print(library.listOfBooks)

print(library.dictOfNumOfBooks)
print(library.listOfBooks)


library = Library("Shin Bet",6,75,2)
c = Client()
c1 = Client()
c1.printClientInfo()
library.addClient(c)
library.addClient(c1)
print(library.listOfClients)
c.printClientInfo()
print(library.listOfClients[0].listOfLibrariesRegisteredTo[0].name)
"""