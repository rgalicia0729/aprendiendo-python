
def verify_prime(n):
    # Verificar si n es un numero primo
    prime = True

    if n == 1:
        prime = False

    for i in range(2, n):
        if (n // 2) < i:
            break

        if n % i == 0:
            prime = False
            break

    return prime


if __name__ == '__main__':
    n = int(input('Verificar si es primo el numero: '))

    print(verify_prime(n))
