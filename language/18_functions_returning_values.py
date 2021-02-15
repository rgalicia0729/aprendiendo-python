# Example 1


def suma(x, y):
    return x + y


result = suma(10, 5)
print(result)

# Example 2


def divide(dividendo, divisor):
    if (divisor != 0):
        return dividendo / divisor
    else:
        return f'No es posible dividir {dividendo} por {divisor}'


result_division = divide(5, 2)
print(result_division)
