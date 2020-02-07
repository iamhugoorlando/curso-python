# -*- coding: utf-8 -*_

# Calcularemos si una palabra es palindromo con Python
# Palindromo son aquellas palabras que se leen igual del derecho y del reves

def palindromo2(word):
    palabra_alreves = word[::-1]

    if palabra_alreves == word:
        return True

    return False



def palindromo(word):
    letra_alreves = []

    for letter in word:
        letra_alreves.insert(0, letter)

    palabra_alreves = ''.join(letra_alreves)

    if palabra_alreves == word:
        return True

    return False


if __name__ == '__main__':
    word = str(raw_input('Escribe una palabra: '))

    #resultado = palindromo(word) # esta es otra forma de resolver el programa y corresponde a la def palindromo
    resultado = palindromo2(word) # corresponde a la def palindromo2 y es otra forma de resolver el programa

    if resultado is True:
        print('{} si es un palindromo.'.format(word))
    else:
        print('{} no es un palindromo.'.format(word))
