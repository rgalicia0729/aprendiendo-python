# Example 1
def suma(x, y):
    return x + y


nums = [4, 5]
print(suma(*nums))

new_nums = {'x': 3, 'y': 3}
print(suma(**new_nums))


# Example 2
def average(*args):
    return sum(args) / len(args)


print(average(70, 70, 70, 70))


# Example 3
def add(*args):
    total = 0

    for value in args:
        total += value

    return total


def multiply(*args):
    total = 1

    for value in args:
        total *= value

    return total


def apply(*args, operator):
    if operator == '+':
        return add(*args)
    elif operator == '*':
        return multiply(*args)
    else:
        print('Operador no valido')


print(apply(1, 2, 3, 4, 5, operator='*'))
