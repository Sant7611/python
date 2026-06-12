# also known as dunder methods

class Book:

    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
       
    
    def __add__(self, other):
        return self.page + other.page
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        else:
            return f'{key} key not found'


book1 = Book('the magic method', 'j.r.r toklen', 12)
book2 = Book('the magic method', 'j.r.r toklen',14)
book3 = Book('the singing garden', 'henrey',45)

print(book3)

print(book1 == book2)

print(book1 +book2)

print(book1['title'])