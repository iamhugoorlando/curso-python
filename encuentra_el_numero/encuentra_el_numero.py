# -*- coding: utf-8 -*-

# Juego encuentra el numero
import random



def run(): # inicializamos la funcion run

    # Escribi mi propio codigo desde la linea 11 hasta la 22
    name = input('Ingresa un numero: ')
    print('Hola ' + name)

    empecemos = 'Si'
    queres_jugar = input('Queres jugar?')
    jugar = queres_jugar

    for i in queres_jugar:
        if jugar == empecemos:
            print('Bien! Empecemos!')
        else:
            print('Lo siento mucho :(')

    # A partir de estas lineas es codigo propio del curso
    # desde las lines 25 al 42 codigo propio del curso
    number_found = False
    random_numer = random.randint(0,20)

    while not number_found:
        number = input('Ingresa un numero: ')

        if number == random_numer:
            print('Felicidades ' + (name) + ',' + ' encontraste el numero!')
            number_found = True
        elif number > random_numer:
            print('El numero es más pequeño')
        else:
            print('El numero es más grande')


if __name__ == '__main__':
    run()
