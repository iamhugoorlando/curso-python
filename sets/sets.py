# sets en python

# son similares a las listas pero no permiten elementos repetidos
# con sets podemos realizar las operaciones basicas de conjuntos, esto quiere decir que se puede calcular
# los valores de intercepcion, diferencia, union

# un set es una coleccion de datos no ordenadas sin datos repetidos. Se puede aplicar para eliminar datos repetidos entre
# dos sets

# declarar sets
s = set([1,2,3])
t = set([3,4,5])

print(s)
print(t)

# operaciones con sets
print(s.union(t))
print(s.intersection(t))
print(s.difference(t))


