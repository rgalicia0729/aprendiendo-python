from random import randrange

if __name__ == '__main__':
    user_input = input('Te gustaría jugar (Y/n): ').lower()

    while user_input == 'y':
        number = randrange(10)

        print('---' * 25 + '\n')
        user_number = int(input('Que número estoy pensando: '))

        if user_number == number:
            print('Felicidades es correcto')
        elif (number - user_number) in (1, -1):
            print('Genial! Eso estuvo muy cerca')
        else:
            print(':( Lo siento, no es correcto, intentalo de nuevo')

        user_input = input('Te gustaría intentarlo de nuevo (Y/n): ').lower()

    print('Fin...')
