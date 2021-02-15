# Ejemplo 1
numbers = [1, 2, 3, 4, 5]
doubles = [x * 2 for x in numbers]

print('Numbers', numbers)
print('Doubles', doubles)

print('---' * 25 + '\n')

# Ejemplo 2
friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
starts_s = [friend for friend in friends if friend.startswith('S')]

print(starts_s)
