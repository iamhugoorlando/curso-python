# -*- coding: utf-8 -*-

# manejo de errores en python

# para manejar errores en python se utiliza try/except
# python tiene una jerarquia de errores
# nace de una exception base

# try / except / else / finally

# construiremos un programa que nos digan la poblacion en millones de los paises de LATAM

paises = {
    'mexico': 122,
    'argentina': 43,
    'colombia': 49,
    'chile': 18,
    'paraguay': 8,
    'brasil': 70
}

# preguntamos el pais a saber la poblacion
while True:
    pais = str(raw_input('Escribe el nombre de un pais: ')).lower()

    try:
        print('La pobacion de {} es: {} millones'.format(pais, paises[pais]))
    except KeyError:
        print('No tenemos la el dato de poblacion de {}'.format(pais))



