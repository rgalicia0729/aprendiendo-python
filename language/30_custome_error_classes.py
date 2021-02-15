class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self, name: str, pages_acout: int):
        self.name = name
        self.pages_acout = pages_acout
        self.pages_read = 0

    def __repr__(self):
        return (
            f'<Book {self.name}, read {self.pages_read} pages of out {self.pages_acout}>'
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.pages_acout:
            raise TooManyPagesReadError(
                f'You tried to read {self.pages_read + pages} pages, but this book only has {self.pages_acout} pages'
            )
        self.pages_read += pages
        print(
            f'You have now read {self.pages_read} pages of out {self.pages_acout}')


try:
    python101 = Book('Pathon101', 50)
    python101.read(30)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)
