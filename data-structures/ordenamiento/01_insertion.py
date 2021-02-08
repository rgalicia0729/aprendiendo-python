
def ascending_order(data):
    i = 1
    while i < len(data):

        j = i
        while j > 0:
            if data[j - 1] > data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
            else:
                break

            j -= 1

        print(data)

        i += 1

    return data


def descending_order(data):
    i = 1
    while i < len(data):

        j = i
        while j > 0:
            if data[j - 1] < data[j]:
                data[j - 1], data[j] = data[j], data[j - 1]
            else:
                break

            j -= 1

        print(data)

        i += 1

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
