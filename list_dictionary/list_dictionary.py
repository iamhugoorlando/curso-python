# list y diccionary comprenhensions en python

# dictionary comprehensions y list comprehensions nos permiten escribir listas o diccionarios de forma mas sencilla

#numeros pares
pares = []
for num in range(1,31):
    if num % 2 == 0:
        pares.append(num)

# esto mismo lo podemos expresar con una list comprehension
par = [num for num in range(1,21) if num % 2 ==0]

print(pares)
print(par)

# ahora lo veremos en un diccionario
ciudades = {}
for num in range(1,8):
    ciudades[num] = num**2

print(ciudades)

city = {num: num**2 for num in range(1,21)}
print(city)