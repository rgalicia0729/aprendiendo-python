# Example 1
a, b = 1, 2

print(f'a: {a}')
print(f'b: {b}')

# Example 2
print('\n')

my_tuple = (5, 10)
x, y = my_tuple

print(my_tuple)
print(f'x: {x}')
print(f'y: {y}')

# Example 3
print('\n')

student_attandance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}
print(list(student_attandance.items()))

for key, value in student_attandance.items():
    print(f'{key}: {value}')
