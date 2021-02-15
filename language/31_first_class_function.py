# Example one


def divide(divided, divisor):
    if divisor == 0:
        raise ZeroDivisionError('Divisor cannot be 0.')

    return divided / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)

# Example two


def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element

    raise RuntimeError(f'Could not find with an element with {expected}')


def get_friend_name(friend):
    return friend['name']


friends = [
    {'name': 'Bob Smith', 'age': 30},
    {'name': 'Adam Wool', 'age': 24},
    {'name': 'Anne Pun', 'age': 27}
]

print(search(friends, 'Bob Smit', get_friend_name))
