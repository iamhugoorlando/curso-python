# -*- coding: utf-8 -*-

# un decorador es una funcion que recibe como parametro a otra funcion y modifica su comportamiento

# un decorador se aplica a una funcion o metodo con el simbolo @ super util para definir si una funcion debe ejecutarse o no

# en servidores web existen ciertas funciones que nada más deben ejecutarse si un usuario se encuentra auntenticado

# vamos a generar una funcion que este protegida por una contraseña

def protected(func):

    def wrapper(password):
        if password == 'holamundo':
            return func()
        else:
            print('La contraseña es incorrecta')

    return wrapper

@protected # definimos nuestro decorador
def protecter_func():
    print('Tu contraseña es correcta')

if __name__ == '__main__':
    password = str(raw_input('Ingresa tu contraseña: '))
    protecter_func(password)

