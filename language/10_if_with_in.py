
if __name__ == '__main__':
    number = 7
    user_input = input('Ingresa (y) si te gustaria jugar: ').lower()

    if user_input == 'y':
        user_number = int(input('Que número estoy pensando: '))
        if user_number == number:
            print('Es correcto')
        else:
            print('No es correcto')
    else:
        print('Ok, esta bien')

    print('Fin del Juego')
