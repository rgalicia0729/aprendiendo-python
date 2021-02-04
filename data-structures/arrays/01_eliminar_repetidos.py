
def eliminar_repetidos(array):
    new_array = []

    for i in array:
        not_repeated = True

        for j in new_array:
            if i == j:
                not_repeated = False
                break

        if not_repeated:
            new_array.append(i)

    return new_array


if __name__ == '__main__':
    numeros = []

    while True:
        try:
            new_number = int(
                input('Ingresa un número entero si deseas continuar: '))

            numeros.append(new_number)
        except:
            break

    print(eliminar_repetidos(numeros))
