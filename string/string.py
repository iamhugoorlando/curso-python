# Cadenas o String en python

# un string es una secuencia de caracteres
# los caracteres se pueden acceder por indice

name = 'Hugo'
print(name[0]) # H
print(name[1]) # u
print(name[2]) # g
print(name[3]) # o


# Para conocer la longitud de un string podemos usar la funcion len

print(len(name)) # 4

print(name.upper()) # retorna el str en mayuscua
print(name.lower()) # retorna el str en minuscula
print(name.find('H')) # retorna el indice donde se encuentre H

# Slices (rebanadas)

# se puede obtener una substring utilizando a notacion Slices
# se definen los rangos que se requieren y los saltos necesarios

hola = 'Hola'
print(hola)
print(hola[1:])
print(hola[1:3]) # no se incluye el indice 3
print(hola[1:6:2]) # recorre todo el str pero en salto de 2
print(hola[::-1]) # acceder al str desde el final al principio
