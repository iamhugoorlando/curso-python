# -*- coding: utf-8 -*-

# Juego encuentra el numero
import random



def run(): # inicializamos la funcion run

    name = str(raw_input('Ingresa tu nombre: '))
    print('Hola ' + name)

    empecemos = 'Si'
    queres_jugar = str(raw_input('Queres jugar?: '))
    jugar = queres_jugar

    for i in queres_jugar:
        if jugar == empecemos:
            print('Bien! Empecemos!')
        else:
            print('Lo siento mucho :(')

    number_found = False
    random_numer = random.randint(0,20)

    while not number_found:
        number = int(raw_input('Ingresa un numero: '))

        if number == random_numer:
            print('Felicidades ' + (name) + ',' + ' encontraste el numero!')
            number_found = True
        elif number > random_numer:
            print('El numero es más pequeño')
        else:
            print('El numero es más grande')


if __name__ == '__main__':
    run()
