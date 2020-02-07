# Aprenderemos sobre diccionarios en python

# un diccionario contiene valores de cualquier tipo
# se crea con {} o con el keyword dict
# los diccionarios trabajan con clave-valor
# nos permiten definir objetos de la vida real: productos, personas, ciudades, etc

productos = {
    'nombre': 'libro',
    'cantidad': 100,
    'precio': 15.45,
    'moneda': 'USD'
}

print(productos)

# podemos obtener solamentes las claves de los diccionarios
print(productos.keys())

# podemos obtener los valores de un diccionario
print(productos.values())

# ademas podemos escrirlo de la sgte forma y agregarlo a la variable productos
productos['ciudad'] = 'Jose C Paz'
print(productos)

calificaciones = {}
calificaciones['algoritmos'] = 9
calificaciones['base de datos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 9

for key in calificaciones:
    print(key)


# nos devuelve una lista de valores
for values in calificaciones.values():
    print(values)

# iterar entre clave y valor
for key, value in calificaciones.items():
    print('llave: {}, valor: {},'.format(key,value))


suma_de_calificaciones = 0
for calificacion in calificaciones.values():
    suma_de_calificaciones += calificacion

print('La suma de calificaciones es: {}'.format(suma_de_calificaciones))

promedio = suma_de_calificaciones / len(calificaciones.values())
print('El promedio es: {}'.format(promedio))



