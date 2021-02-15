# Example 1
friends_ages = {'Rolf': 17, 'Adam': 30, 'Anne': 27}

friends_ages['Antony'] = 40

print(friends_ages['Adam'])
print(friends_ages)

# Example 2
print('\n')
friends = [
    {'name': 'Rolf', 'age': 17},
    {'name': 'Adam', 'age': 30},
    {'name': 'Anne', 'age': 27}
]

print(friends[1]['name'])
print(friends)

# Example 3
print('\n')
student_attandance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}

for student in student_attandance:
    print(f'{student}: {student_attandance[student]}')

# Example 4
print('\n')

for student, attandance in student_attandance.items():
    print(f'{student}: {attandance}')

# Example 5
print('\n')

student = 'Bob'

if student in student_attandance:
    print(f'Bob: {student_attandance[student]}')
else:
    print(f'{student} is not a student in this class')

# Example 6
print('\n')

attandance_values = student_attandance.values()
average = (sum(attandance_values) / len(attandance_values))
print(f'Average: {average}')
