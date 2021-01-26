# Encontrar la diferencia entre dos numeros enteros sin utilizar el operador (-)


def diferencia_de_enteros(a, b):
    result = 0

    while a > b:
        b += 1
        result += 1

    return result


if __name__ == '__main__':
    numero_uno = int(input('Ingresa el valor de numero uno: '))
    numero_dos = int(input('Ingresa el valor de numero dos: '))

    resultado = 'La diferencia entre {} y {} es: {}'
    diferencia = 0

    if numero_uno > numero_dos:
        diferencia = diferencia_de_enteros(numero_uno, numero_dos)
    else:
        diferencia = diferencia_de_enteros(numero_dos, numero_uno)

    print(resultado.format(numero_uno, numero_dos, diferencia))
