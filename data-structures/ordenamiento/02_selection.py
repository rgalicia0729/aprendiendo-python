
def ascending_order(data):
    # Algoritmo selection para ordenar un array de numeros

    for i in range(len(data)):
        index_select = i
        for j in range(i, len(data)):
            if data[j] < data[index_select]:
                index_select = j

        data[i], data[index_select] = data[index_select], data[i]
        print(data)

    return data


def descending_order(data):
    # Algoritmo selection para ordenar un array de numeros

    for i in range(len(data)):
        index_select = i
        for j in range(i, len(data)):
            if data[j] > data[index_select]:
                index_select = j

        data[i], data[index_select] = data[index_select], data[i]
        print(data)

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
