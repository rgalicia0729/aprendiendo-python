
def division_algorithm(dividendo, divisor):
  # Dividir sin utilizar el operador (/)
    result = 0

    while (dividendo - divisor) >= 0:
        dividendo -= divisor
        result += 1

    if dividendo > 0:
        result = f'{result}.{dividendo}'
        float(result)

    return result


if __name__ == '__main__':
    dividendo = 15
    divisor = 3

    print(f'{dividendo} / {divisor} = {division_algorithm(dividendo, divisor)}')
