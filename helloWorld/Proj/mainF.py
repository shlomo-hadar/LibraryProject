from Proj.module import *

library = Library("bet",90,75,2)
book = Book("the red lotus","van dam",1974,5,5,5)
book2 = Book("the red lotus","van dam",1974,5,5,5)
book3 = Book("the red lotus","van dam",1974,5,5,5)
print(library.DictOfNumOfBooks)
print(library.ListOfBooks)
library.addBook(book)
library.addBook(book2)
library.addBook(book3)
print(library.DictOfNumOfBooks)
print(library.ListOfBooks)
print(library.printListOfBooks())