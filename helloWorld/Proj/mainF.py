from Proj.library import *
from Proj.book import Book
from Proj.client import *
from random import randint as r


# library = Library("Shin Bet", 6, 75, 2)
# book = Book("the red lotus", "van dam", 1974, r(2,10), r(2,10), r(2,10))   # the red lotus by van dam
# book2 = Book("the red lotus2", "van dam", 1977, r(2,10), r(2,10), r(2,10))
# book3 = Book("the red lotus3", "van dam", 1984, r(2,10), r(2,10), r(2,10))
# library.add_book(book)
# library.add_book(book2)
# library.add_book(book3)
# library.remove_book()
# print(library.print_list_of_books())
# book.print_book_info()
# client = Client("abb", "lin", r(2,10), r(2,10), r(2,10), r(2,20), [])
# library.add_client(client)
# print(library.list_of_clients[0].first_name)
# print(library.list_of_clients[0].last_name)
# print(library.list_of_clients[0].id)
# client.recommend_on_the_best_suitable_book()
# client.borrow_book()
# client.return_book()
# library.remove_customer()
#
#
# print(len(client.print_books_in_possetion()))
#
#
# print(library.dict_of_num_of_books)
# print(library.list_of_books)
#
# print(library.dict_of_num_of_books)
# print(library.list_of_books)
#
#
# library = Library("Shin Bet",6,75,2)
# c = Client()
# c1 = Client()
# c1.print_client_info()
# library.add_client(c)
# library.add_client(c1)
# print(library.list_of_clients)
# c.print_client_info()
# print(library.list_of_clients[0].list_of_libraries_registered_to[0].name)

def test_book_str():
    my_book = Book(title="t", author="a", publication_year=2000, comic=1, dramatic=2, educational=3)
    if str(my_book) != "[t, a, 2000, 1, 2, 3]":
        print("ERROR: str(book) was erroneously " + str(my_book))
        exit(-1)


def main():
    test_book_str()


if __name__ == '__main__':
    main()
