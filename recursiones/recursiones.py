# -*- coding: utf-8 -*-

# Factorial de un numero con recursiones en python

# recursion: una función está siendo recursiva cuando dentro
# del bloque de instrucciones que la conforma se usa a sí misma.
# por ejemplo cuando haces el calculo del factorial de un número
# lo haces con una función recursiva:
# El factorial de un número es el número multiplicado por los números antes de el,
# 5! es 5*4*3*2*1

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

if __name__ == '__main__':
    n = int(raw_input('Escribe un numero: '))

    resultado = factorial(n)
    print(resultado)
