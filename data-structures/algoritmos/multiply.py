
def multiply_algorithm(x, y):
    # Multiplicar sin utilizar el operador (*)
    result = 0
    factor_a = 0
    factor_b = 0

    if x == y or x > y:
        factor_a = x
        factor_b = y
    elif x < y:
        factor_a = y
        factor_b = x

    for _ in range(factor_b):
        result += factor_a

    return result


if __name__ == '__main__':
    a = 15
    b = 3

    print(f'{a} x {b} = {multiply_algorithm(a, b)}')
