
def pow_algorithm(base, exp):
    # Potencia sin utilizar el operador
    result = 1

    for _ in range(exp):
        result *= base

    return result


if __name__ == '__main__':
    base = 2
    exp = 3

    print(f'{base} ^ {exp} = {pow_algorithm(base, exp)}')
