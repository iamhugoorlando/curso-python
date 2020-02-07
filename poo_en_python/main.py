# -*- coding: utf-8 -*-

from lamp import Lamp

# aqui declaramos una instancia nueva de la clase
def run():
    lamp = Lamp(is_turned_on=False)

    while True:
        command = str(raw_input('''            
                ¿Que desea hacer?

                [p]render
                [a]pagar
                [s]alir            
            '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break


if __name__ == '__main__':
    run()