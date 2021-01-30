
def substract_algorithm(x, y):
    # Restar sin utilizar el operador (-)
    result = 0

    if x > y:
        for _ in range(y, x):
            result += 1

    return result


if __name__ == '__main__':
    a = 15
    b = 5

    print(f'{a} - {b} = {substract_algorithm(a, b)}')
