class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
        
    def description(self, publisher = "Diogene"):
        return f"{self.title} by {self.author}, {self.pages} pages, is published by {publisher} "
        

book1 = Book("1984", "George Orwell", 328)
print(book1.description("Merani"))

