# Example 1
def named(**kwargs):
    print(kwargs)


named(name='Rigo', age=29)


# Example 3
def print_named(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_named(name='Rigo', ege=29)


# Example 4
def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, name='Rigo', ege=29)
