from time import time


def ascending_order(data):
    # Algoritmo de ordenamiento selection de forma ascendente
    tiempo_inicial = time()

    for i in range(len(data)):
        index_select = i
        for j in range(i, len(data)):
            if data[j] < data[index_select]:
                index_select = j

        data[i], data[index_select] = data[index_select], data[i]

    tiempo_final = time()
    tiempo_ejecucion = (tiempo_final - tiempo_inicial) * 1000
    print(f'\nEl tiempo de ejecución es: {tiempo_ejecucion} segundos')

    return data


def descending_order(data):
    # Algoritmo de ordenamiento selection de forma descendente
    tiempo_inicial = time()

    for i in range(len(data)):
        index_select = i
        for j in range(i, len(data)):
            if data[j] > data[index_select]:
                index_select = j

        data[i], data[index_select] = data[index_select], data[i]

    tiempo_final = time()
    tiempo_ejecucion = (tiempo_final - tiempo_inicial) * 1000
    print(f'\nEl tiempo de ejecución es: {tiempo_ejecucion} segundos')

    return data


if __name__ == '__main__':
    data = [-3, 2, 7, 1, 5, 0, 4, 3, 8, -1, 2, 4, 6, 9, 10, 2, -2, 25, 67, 89,
            98, 111, 128, 4356, 18982, 45, 34, 55, 67, 54, 56, 23, 23, 67, 68, 90, 20]

    print(('-' * 25) + 'Entrada' + ('-' * 25))
    print(data)
    print('\n')

    print(('-' * 25) + 'Ascending' + ('-' * 25))
    print(ascending_order(data))
    print('\n')

    print(('-' * 25) + 'Descending' + ('-' * 25))
    print(descending_order(data))
    print('\n')
