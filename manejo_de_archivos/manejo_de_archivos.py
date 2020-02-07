# manejo de archivos en python

# python puede leer y escribir archivos con la funcion open
# la funcion open regresa un objeto archivo (file)
# los archivos pueden ser de texto o binarios
# se tiene que especificar el modo en que se maneja el archivo

# r = read
# w = write
# a = append
# r+ = read and write

# se debe cerrar el archivo con el metodo close
# la mejor manera de manejar archivos es con el keyword with

# lectura de archivo

def run():
    with open('numeros.txt', 'w') as f:
        for i in range(10):
            f.write(str(i))

if __name__ == '__main__':
    run()