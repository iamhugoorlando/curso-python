# Operaciones con listas en python

# las listas soportan los operadores + y -

mi_lista = []
print(type(mi_lista))
print('')

mi_lista.append(1)
mi_lista.append('Hugo')
mi_lista.append('Gabi')

print(mi_lista)
print('')

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) # en una sola lista ingresan los valores de a y b
print('')

# las listas soportan slices
lista = [1,2,3,4,5,6,7,8,9]
print(lista)
print(lista[1:])
print(lista[1:3])
print(lista[1:6:2])
print(lista[::-1])
print('')

meses = ['Julio', 'Agosto', 'Septiembre']
print(meses[2])

ciudades = list('paris')
print(ciudades)
