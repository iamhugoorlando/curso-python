# Iteraciones

# las iteraciones permiten la misma secuencia de pasos varias veces
# tambien permiten recorrer una secuencia (como un string)
# es una de las herramientas claves de un programador

#funcion range nos permite generar un rango a partir de un numero

a = range(5) # genera una secuencia de numeros de 0 a 5
print(a) # [0, 1, 2, 3, 4]

# si queremos generar un rango del 5 al 20 en pasos de 2
b = range(5, 20,2)
print(b) # [5, 7, 9, 11, 13, 15, 17, 19]

# for es una forma de iterar
for i in range(10):
    print(i)

for j in range(5):
    print('Hola Mundo')


# for loop
# se puede utilizar para recorrer string
# se necesita el keyword "in"
# si se necesita salir antes de la iteracion se utiliza el keyword "break"
# si se requiere pasar a la sgte iteracion se utiliza "continue"

for i in range(30): # rango de 30
    if i % 3 != 0: # si i modulo de 3 es distinto a 0
        continue
    else:
        print(i**2) # elevamos i al cuadrado

for j in range(30):
    if i % 3 == 0:
        print(i**2)
    elif i == 22:
        break

for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break

# recorremos las letras de un string
nombre = 'Paraguay'
for letras in nombre:
    print(letras)
