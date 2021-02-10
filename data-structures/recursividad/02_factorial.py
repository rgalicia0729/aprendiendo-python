
def factorial(number):
    # Calcular el factorial de un numero utilizando la recursividad

    if number > 1:
        number = number * factorial(number - 1)

    return number


if __name__ == '__main__':
    n = int(input('Find the factorial of: '))

    print(f'El factorial de !{n} es: {factorial(n)}')
