# -*- coding: utf-8 -*-

# Busqueda binaria en Python

# busqueda binaria: si queremos saber si un numero se encuentra en una lista, buscamos un item tras otro
# pero si la lista es muy larga esta forma no es mas eficiente.
# la forma mas eficiente es a traves de una busqueda binaria

# con el algoritmo de busqueda binaria partimos de la lista ordenada, seleccionamos un numero aleatorio
# para dividir la lista. Puedo escoger cualquier numero.
# en este caso sumamos el primer y el ultimo indice de la lista, lo sumamos y dividimos en dos(por eso se llama binario)
# luego comparamos el numero que esta en en el indice, de esta manera ya eliminamos la mitad de las opciones
# podemos continuar dividiendo la lista y comparando hasta que lleguemos al resultado esperado

def busqueda_binaria(numeros, number_to_find, low, high):

    if low > high:
        return False

    mid = (low + high) / 2

    if numeros[mid] == number_to_find:
        return True

    elif numeros[mid] > number_to_find:
        return busqueda_binaria(numeros, number_to_find, low, mid - 1)
    else:
        return busqueda_binaria(numeros,number_to_find, mid + 1, high)


if __name__ == '__main__':
    numeros = [1, 3,4,5,6,9,10,11,25,27,28,34,36,49,51]

    number_to_find = int(raw_input('Ingresa un numero: '))

    # llamamos a la funcion busqueda binaria
    resultado = busqueda_binaria(numeros, number_to_find, 0, len(numeros) -1)

    if resultado == True:
        print('El numero si esta en la lista')
    else:
        print('El numero no esta en la lista')