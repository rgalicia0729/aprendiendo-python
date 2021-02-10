
def countdown(num):
    # Algoritmo de cuenta regresiva utilizando la recursividad
    print(num)

    if num > 0:
        countdown(num - 1)
    else:
        print('BOOM')


if __name__ == '__main__':
    num = int(input('Enter a positive whole number: '))

    countdown(num)
