class Library:
    number_of_books = 0

    def __init__(self, list_of_books):

        self.name = input("Library's name")
        self._library = []

        if type(list_of_books) == list:
            for book in list_of_books:
                self._library.append(book)
            Library.number_of_books += len(self._library)
            print("The {} created. There are {} elements in the collection.".format(self.name,Library.number_of_books))
        else:
            print("Invalid collection. Created Library is empty. If You want to add an element to the collection, use the add_book command.")

    @property
    def library(self):
        return self._library

    @library.setter
    def add_book(self, book):
        if self._library.count(book) == 1:
            print("This book is already in {}.".format(self.name))
        else:
            self._library.append(book)
            Library.number_of_books += 1

    def borrow_book(self,book):
        if book in self._library:
            self._library.remove(book)

    def show_books(self):
        print(self._library)

library1 = Library(["Siała baba mak","Piotruś Pan"])

library1.add_book = "Władca much"

library1.show_books()

library1.borrow_book("Siała baba mak")

library1.show_books()
