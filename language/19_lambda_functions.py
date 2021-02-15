# Example 1
def sumar(x, y): return x + y


print(sumar(5, 5))

# Example 2
print((lambda x, y: x + y)(5, 5))


# Example 3


def double(x):
    return x * 2


lista = [1, 2, 3, 4, 5]

lista_dobles = [double(x) for x in lista]

print(lista_dobles)

# Example 4


def triples(x):
    return x * 3


secuencia = [6, 7, 8, 9, 10]

lista_triples = list(map(triples, secuencia))

print(lista_triples)

# Example 5

pares = [2, 4, 6, 8, 10]

pares_por_cinco = [(lambda x: x * 5)(x) for x in pares]

print(pares_por_cinco)

pares_por_dies = list(map((lambda x: x * 10), pares))

print(pares_por_dies)
