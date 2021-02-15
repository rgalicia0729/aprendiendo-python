class Person:
    def __init__(self, name, ege):
        self.name = name
        self.ege = ege

    def __str__(self):
        return f'Name: {self.name}, Ege: {self.ege}'

    def __repr__(self):
        return f'<Person(\'{self.name}\', {self.ege})>'


person = Person('Rigo', 29)
print(person)
