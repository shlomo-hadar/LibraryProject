ID = 0


class Client:
    def __init__(self, first_name="Shniki", last_name="Abutbul", comic=0, dramatic=0, educational=0, joy_threshold=0,
                 list_of_libraries_registered_to=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.id = self.set_id()
        self.comic = comic
        self.dramatic = dramatic
        self.educational = educational
        self.joy_threshold = joy_threshold
        self.list_of_libraries_registered_to = list_of_libraries_registered_to
        self.list_of_books_in_possetion = []

    def set_id(self):
        #  setting the current user id and ascending it for the next customer
        global ID
        ID += 1
        return ID

    def __str__(self):
        """
        prints out the book information
        :return: the string representation of the book
        """
        return self.first_name + " " + self.last_name

    def borrow_book(self):
        #  executing the act of book borrowing by client
        success = 0
        needed_book = input("which book would you like to borrow? ")
        for lib in self.list_of_libraries_registered_to:
            if needed_book in lib.dict_of_num_of_books:  # checks if the book is in the library
                if lib.dict_of_num_of_books[needed_book] > 0:  # checks if the book is in inventory  #####and
                    # checks if the the client can borrow more books from the library
                    if self.authenticate_limit_of_books_possessed(lib):
                        lib.dict_of_num_of_books[needed_book] -= 1
                        for cur_book in lib.list_of_books:
                            if (needed_book == cur_book.title + " by " + cur_book.author) and cur_book.current_holder == lib.name:
                                cur_book.current_holder = self.first_name + " " + self.last_name
                                self.list_of_books_in_possetion.append(cur_book)
                                print("the borrow of the book " + cur_book.title + " by " + cur_book.author + " was completed successfully\n")
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
    #
    # def borrow_book(self):
    #     # interface
    #     book_id = input("which book would you like to borrow? ")
    #     for lib in self.listOfLibrariesRegisteredTo:
    #         msg = lib.attempt_borrow(self, book_id)
    #         if len(msg) == 0:
    #             break
    #         else:
    #             print(msg)
    #
    # def attempt_borrow(self, user, book_id):
    #     if user.authenticateLimitOfBooksPossessed(self):
    #         return "you have reached the maximum of books you can borrow at the same time"
    #     if book_id in self.book_index and len(self.book_index[book_id]) > 0:  # book_index: dict(book_id -> list(book))
    #         real_book = self.book_index[book_id][0]
    #         user.add_book(real_book)
    #         del self.book_index[book_id][0]
    #         return ""
    #     else:
    #         return "we don't have this book in our inventory.. try again later :)"

    def return_book(self):
        #  executing the returning of a book from the customer to the library
        if len(self.list_of_books_in_possetion) == 0:
            print("you have not borrowed any books yet\n")
            return
        book_to_be_returned = input("what book would you like to return?")
        book_returned = 0
        for book in self.list_of_books_in_possetion:
            check = book.title + " by " + book.author
            if book_to_be_returned == check:
                book.current_holder = book.hosting_library
                for lib in self.list_of_libraries_registered_to:
                    if book.hosting_library == lib.name:
                        lib.dict_of_num_of_books[book_to_be_returned] += 1
                        del self.list_of_books_in_possetion[self.find_index(check)]
                        book_returned = 1
                        break
                if book_returned == 1:
                    print("the book " + book.title + " by " + book.author + " was returned successfully")
                    break
        if book_returned == 0:
            print("your are not the borrower of the named book")

    def print_books_in_possetion(self):
        #  returns a string which contains the info of the books which are currently in the customer hands
        inf = ""
        i = 1
        for book in self.list_of_books_in_possetion:
            inf += "book" + str(
                i) + ":\n\t" + book.title + " by " + book.author + "\n\t" + "Current Holder: " + book.current_holder \
                   + "\n\t" + "Hosting Library: " + book.hosting_library + "\n\n"
            i += 1
        return inf

    def authenticate_limit_of_books_possessed(self, lib):
        #  making sure that the number of books that are in the hand of the customer are less than the maximum of books
        #  that could be lended to a certain customer by the library policy
        num_of_books_from_the_lib = 0
        for book in self.list_of_books_in_possetion:
            if book.hosting_library == lib.name:
                num_of_books_from_the_lib += 1
        if num_of_books_from_the_lib < lib.max_num_of_lended_books:
            return 1
        return 0

    def authenticate_joy_level(self, client, book):
        #  to make sure that the book will be joyful to the customer
        if client.comic * book.client + client.dramatic * book.dramatic + client.educational * book.educational >= client.joiThreshold:
            return 1
        else:
            return 0

    def recommend_on_the_best_suitable_book(self):
        most_suitable = ["", 0]
        for lib in self.list_of_libraries_registered_to:
            for book in lib.list_of_books:
                if (book.comic * self.comic + book.dramatic * self.dramatic + book.educational * self.educational) >= self.joy_threshold \
                        and (book.comic * self.comic + book.dramatic * self.dramatic + book.educational * self.educational) > most_suitable[1]:
                    most_suitable[0] = book.title + " by " + book.author
                    most_suitable[1] = book.comic * self.comic + book.dramatic * self.dramatic + book.educational * self.educational
        print("the recommended book for you is " + most_suitable[0] + " with a score of: " + str(most_suitable[1]) + "\n")

    def find_index(self, book_to_drop):
        #  find the index of a book in the list of the books that are in the hands of the customer
        i = 0
        for book in self.list_of_books_in_possetion:
            if book_to_drop == book.title + " by " + book.author:
                return i
            i += 1
