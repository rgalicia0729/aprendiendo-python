
class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'BookShelf with {len(self.books)} books.'


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book {self.name}'


book_one = Book('Harry Potter')
book_two = Book('Python')

book_shelf = BookShelf(book_one, book_two)

print(book_shelf)
