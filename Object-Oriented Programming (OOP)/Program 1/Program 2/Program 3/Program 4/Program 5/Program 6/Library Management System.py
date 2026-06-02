class Book:

    def __init__(self, title):
        self.title = title

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(title, "Issued")
                return
        print("Book Not Available")

    def return_book(self, book):
        self.books.append(book)
        print(book.title, "Returned")

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(book.title)

library = Library()

b1 = Book("Python Basics")
b2 = Book("Data Structures")

library.add_book(b1)
library.add_book(b2)

library.display_books()

library.issue_book("Python Basics")

library.display_books()

library.return_book(b1)

library.display_books()