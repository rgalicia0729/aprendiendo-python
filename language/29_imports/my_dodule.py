from my_lib import is_str


def hello_name(name):
    if is_str(name):
        print(f'Hello, {name}')
    else:
        print(f'{name} is not a String')


print(__name__)
