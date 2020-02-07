# -*- coding: utf-8 -*-

# Practicaremos funciones creando una tortuga
# a partir de la tortuga que ya hemos creado en el archivo
# tortuga.py

import turtle

# definimos la funcion main
def main():
    windows = turtle.Screen() # windows recibe la tortuga
    david = turtle.Turtle() # david es el nombre de la tortuga
    make_square(david) # Creamos la funcion make_square que recibe a david como parametro

    turtle.mainloop() # permite que la ventana no cierre

# funcion make_square que iniciara el cuadrado
# recibe como parametro a david
# make_square nos permite pedir al usuario que ingrese el tamaño del cuadrado
def make_square(david):
    lenght = int(raw_input('Tamaño de cuadrado: ')) # el user ingresara el tamaño del cuadrado

    # range es una funcion que permite generar valores a un rango de 4
    for i in range(4): # recorre range hasta un rango de 4

        # make_line_and_turn recibe el parametro david y el tamaño que tendra
        #para luego ingresarlo en otra funcion con su mismo nombre
        make_line_and_turn(david, lenght)

# creamos la funcion make_line_and_turn con parametros david y lengtu
def make_line_and_turn(david, length):
    david.forward(length) # recibe el tamaño que ingreso el user
    david.left(90) # recibe 90 como linea

if __name__ == '__main__': # definimos donde empieza nuestro programa
    main() # ejecutamos nuestra funcion main
