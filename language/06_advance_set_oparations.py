students = {"Rolf", "Anna", "Lucia", "Bob"}
friends = {"Lucia", "Rolf", "Carlos"}

not_friends = students.difference(friends)
print(f'Not friends: {not_friends}')
print('---' * 30)

people = students.union(friends)
print(f'People: {people}')
print('---' * 30)

students_and_friends = students.intersection(friends)
print(f'Studetns and friends: {students_and_friends}')
