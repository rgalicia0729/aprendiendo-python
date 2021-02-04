
def factorial_algorithm(n):
    # Calculo de factorial
    result = 1

    for i in range(n):
        result *= (i + 1)

    return result


if __name__ == '__main__':
    n = int(input('Encontrar el factorial de: '))

    print(f'El factorial de {n} es: {factorial_algorithm(n)}')
