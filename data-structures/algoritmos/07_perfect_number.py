

def is_perfect_number(number):
    # Algoritmo para saber si un numero es perfecto
    sum_of_divisors = 0

    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == number:
        return True
    else:
        return False


if __name__ == '__main__':
    number = int(input('Enter the integer number: '))

    print(f'{number} es un número perfecto' if is_perfect_number(
        number) else f'{number} no es un número perfecto')
