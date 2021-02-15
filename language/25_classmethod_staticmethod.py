class ClassTest:
    def instance_method(self):
        print(f'Called instance method of {self}')

    @classmethod
    def class_method(cls):
        print(f'Called class method of {cls}')

    @staticmethod
    def static_method():
        print(f'Called static method ...')


test = ClassTest()
test.instance_method()

ClassTest.class_method()

ClassTest.static_method()


class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, {self.weight}g>'

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


hardcover_book = Book.hardcover('Harry Potter', 1500)
paperback_book = Book.paperback('Harry Potter', 1500)

print(hardcover_book)
print(paperback_book)
