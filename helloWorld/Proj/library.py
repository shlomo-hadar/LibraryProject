
class Library:
    def __init__(self, name="default", max_num_of_books=100, max_num_of_customers=50,
                 max_num_of_lended_books=2, list_of_books=[], dict_of_num_of_books={}, list_of_clients=[]):
        # the information of an independent library
        self.name = name  # library name
        self.num_of_books = 0  # current number of books that the library is hosting
        self.max_num_of_books = max_num_of_books  # maximum books that the library can host
        self.num_of_customers = 0  # current amount of clients
        self.max_num_of_customers = max_num_of_customers  # maximum amount of clients
        self.max_num_of_lended_books = max_num_of_lended_books  # maximum books that a client can borrow at the same time
        self.list_of_books = list_of_books  # contains a book class objects
        self.dict_of_num_of_books = dict_of_num_of_books  # keeps track of the amount of copies of each individual book
        self.list_of_clients = list_of_clients  # list of the library clients

    def add_book(self, book):
        #  adds a new book to the library
        if self.num_of_books != self.max_num_of_books:
            self.list_of_books.append(book)
            if (book.title + " by " + book.author) in self.dict_of_num_of_books:
                self.dict_of_num_of_books[book.title + " by " + book.author] += 1
                book.current_holder = self.name
                book.hosting_library = self.name
                self.num_of_books += 1
            else:
                self.dict_of_num_of_books[book.title + " by " + book.author] = 1
                book.current_holder = self.name
                book.hosting_library = self.name
                self.num_of_books += 1
        else:
            print("book addition failed")

    def add_client(self, client):
        #  adding the client to the list of client in the library object
        #  and the library to the list of the client registered libraries list
        if client not in self.list_of_clients:
            self.list_of_clients.append(client)
            client.list_of_libraries_registered_to.append(self)

    def print_list_of_books(self):
        #  prints the books of a library with all of their info
        i = 1
        listInf = ""
        for book in self.list_of_books:
            listInf += "book " + str(
                i) + ": \n\t" + "Title: " + book.title + "\n\tAuthor: " + book.author + "\n\tYear Of Publication: " \
                       + str(book.publication_year) + "\n\tComic Value: " + str(
                book.comic) + "\n\tDramatic Value: " + str(book.dramatic) \
                       + "\n\tEducational Value: " + str(book.educational) + "\n\n"
            i += 1
        return listInf

    def remove_book_from_library(self):
        book_to_remove = input("what book should the system erase from the library? ")
        i = 0
        count = 0
        deletion_success = 0
        book_who_got_deleted = ""
        for book in self.list_of_books:
            check = book.title + " by " + book.author
            if check == book_to_remove:
                book_who_got_deleted = check
                del self.list_of_books[i]
                deletion_success = 1
                count += 1
        if deletion_success == 1:
            print("the book " + book_who_got_deleted + " was erased from the library in " + str(count) + " copies")

    def remove_customer_from_library(self):
        first_name = input("what is the first name of the customer you would like to erase from the system? ")
        last_name = input("what is his last name? ")
        id = int(input("what is his id? "))
        i = 0
        deletion_success = 0
        for customer in self.list_of_clients:

            if customer.first_name == first_name and customer.last_name == last_name and customer.id == id:
                del self.list_of_clients[i]
                deletion_success = 1
                i += 1
            if deletion_success == 1:
                break
        if deletion_success == 1:
            print("the client " + first_name + " " + last_name + " id: " + str(id) + ", was erased from the library")
