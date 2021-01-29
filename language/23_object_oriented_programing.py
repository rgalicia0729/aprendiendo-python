class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades) / len(self.grades)


student = Student('Rigo', (90, 91, 95, 100))

print(f'Name: {student.name}')
print(f'Average grades: {student.average_grades()}')
