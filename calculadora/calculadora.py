# -*- coding: utf-8 -*-

# vamos a construir un programa que nos permite determinar si un número
# es primo o no, usando expresiones booleanas, operadores relacionales y operadores lógicos.

# Todas las funciones deben declararse con el keyword def
# Un bug es un error en el código y requiere ser verificado

def es_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero % 2 == 0:
        return False
    else:
        for i in range(3, numero):
            if numero % i == 0:
                return False


    return True


def run():
    # pass # es una forma de decir a python que acabamos de definir una funcion
    numero = int(raw_input('Ingresa un numero: '))
    resultado = es_primo(numero)

    if resultado is True:
        print('El numero es primo')
    else:
        print('El numero no es primo')

    # generar una funcion llamada es_primo que tendra un parametro numero
    es_primo(numero)

# Aqui iniciara nuestro programa
if __name__ == '__main__':
    run()
