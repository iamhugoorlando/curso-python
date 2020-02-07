# -*- coding: utf-8 -*-

def average_temps(temperaturas): # creamos la def average_temps con el parametro temperaturas
    suma_de_temp = 0 # inicializamos en 0 la variable que guardara la suma de temperaturas

    for temps in temperaturas: # recorremos la temperatura
        suma_de_temp += float(temps) # sumamos la temperaturas y guardamos en una variable

    return suma_de_temp / len(temperaturas) # retornamos la suma de temp dividido la cantidad de temperaturas de la list


if __name__ == '__main__':
    temperaturas = [28, 32, 26, 35, 26, 38] # creamos la lista temperaturas

    average = average_temps(temperaturas) # asignamos la variable average para que guarde el resultado de la def average_temps

    print('La temperatura promedio es:  {}'.format(average))
