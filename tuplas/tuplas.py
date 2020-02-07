# tuplas en python

# las tuplas son una secuencia de valores indexada por enteros (integers)
# similares a las listas, con la diferencia de que no pueden cambiarse o modificarse

# las tuplas se crean separando los valores con comas y van dentro de parentesis

# vamos a construir un programa que nos permita encontrar el primer caracter que no se repite en un string

"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {}

    for i, letter in enumerate(char_sequence):
        if letter not in seen_letters:
            seen_letters[letter] = (i, 1)
        else:
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1)

    final_letters = []
    for key, value in seen_letters.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))