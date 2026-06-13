class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)   # created inside
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]
    
class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library('Santosh')
library.add_book('santosh hero', 'santosh')

print(library.list_books())