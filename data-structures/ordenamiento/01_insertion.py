from time import time


def ascending_order(data):
    # Algoritmo de ordenamiento insertion de forma ascendente
    tiempo_inicial = time()

    i = 1
    while i < len(data):

        j = i
        while j > 0:
            if data[j - 1] < data[j]:
                break

            data[j - 1], data[j] = data[j], data[j - 1]

            j -= 1

        i += 1

    tiempo_final = time()
    tiempo_ejecucion = (tiempo_final - tiempo_inicial) * 1000
    print(f'\nEl tiempo de ejecución es: {tiempo_ejecucion} segundos')

    return data


def descending_order(data):
    # Algoritmo de ordenamiento insertion de forma descendente
    tiempo_inicial = time()

    i = 1
    while i < len(data):

        j = i
        while j > 0:
            if data[j - 1] > data[j]:
                break

            data[j - 1], data[j] = data[j], data[j - 1]

            j -= 1

        i += 1

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
