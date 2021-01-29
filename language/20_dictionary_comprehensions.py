users = [
    (0, 'Bob', 'password'),
    (1, 'Rolf', 'rol1234'),
    (2, 'Jose', 'long4password'),
    (3, 'Rosa', '123456')
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
