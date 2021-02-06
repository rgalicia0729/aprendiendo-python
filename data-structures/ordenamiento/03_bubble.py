
def ascending_order(data):
    # Algoritmo de ordenamiento bubble de forma ascendente
    rounds = 0
    organized = False

    while not organized:
        organized = True

        for i in range((len(data) - 1) - rounds):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                organized = False

        print(data)
        rounds += 1

    return data


def descending_order(data):
    # Algoritmo de ordenamiento bubble de forma descendente
    rounds = 0
    organized = False

    while not organized:
        organized = True

        for i in range((len(data) - 1) - rounds):
            if data[i] < data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                organized = False

        print(data)
        rounds += 1

    return data


if __name__ == '__main__':
    data = [-3, 2, 7, 1, 5, 0, 4, 3, 8, -1, 2, 4, 6, 9, 10, 2, -2]

    print(('-' * 25) + 'Entrada' + ('-' * 25))
    print(data)
    print('\n')

    print(('-' * 25) + 'Ascending' + ('-' * 25))
    print(ascending_order(data))
    print('\n')

    print(('-' * 25) + 'Descending' + ('-' * 25))
    print(descending_order(data))
    print('\n')
