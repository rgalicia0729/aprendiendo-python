# Funciones en python

# Example 1


def hello(name):
    print(f'Hello, {name}')


hello('Rigo Galicia')

# Example 2

friends = []


def add_friends():
    friend = input('Enter your name friend: ')
    friends.append(friend)


while True:
    opc = input('Quieres agregar un amigo Y/n? ').lower()

    if (opc != 'y'):
        break

    add_friends()

print(friends)
