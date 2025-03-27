class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_available = True  # Private attribute

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return f"You have borrowed '{self.title}'"
        return f"'{self.title}' is currently not available"

    def return_book(self):
        self.__is_available = True
        return f"'{self.title}' has been returned"

    def is_available(self):
        return self.__is_available


class Library:
    def __init__(self):
        self.__books = []  # Private list of books

    def add_book(self, title, author):
        book = Book(title, author)
        self.__books.append(book)
        return f"Book '{title}' added to the library"

    def list_books(self):
        return [f"{book.title} by {book.author} - {'Available' if book.is_available() else 'Borrowed'}" for book in self.__books]

    def borrow_book(self, title):
        for book in self.__books:
            if book.title == title:
                return book.borrow()
        return "Book not found"

    def return_book(self, title):
        for book in self.__books:
            if book.title == title:
                return book.return_book()
        return "Book not found"
# გამოყენება
library = Library()
library.add_book("Python Basics", "John Doe")
library.add_book("Data Science", "Jane Doe")
print(library.list_books())
print(library.borrow_book("Python Basics"))
print(library.list_books())
print(library.return_book("Python Basics"))
print(library.list_books())
