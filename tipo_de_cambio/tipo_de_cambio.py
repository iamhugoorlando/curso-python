# -*- coding: utf-8 -*-

# Construiremos una calculadora de divisas desarrollando funciones

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('Convierte pesos mexicanos a pesos colombianos')
    print('')

    # guardamos los valores en una variable cantidad
    ammount = float(raw_input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))

    # asignamos el resultado en una variable
    result = foreign_exchange_calculator(ammount)
    print('${} pesos mexicanos son ${} pesos colombianos')
    print('')

    # vamos a generar un def que nos calcule este tipo de cambio
    foreign_exchange_calculator(ammount)

# generamos un def que recibe la cantidad
def foreign_exchange_calculator(ammount): # recibe como parametro la cantidad
    mex_to_col_rate = 145.77 # valor del tipo de cambio
    return mex_to_col_rate * ammount



# indicamos desde donde ejecutara nuestro programa
if __name__ == '__main__':
    run()
    print('Final')
