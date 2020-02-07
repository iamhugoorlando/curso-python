# Primeros pasos en Python
# En este ejemplo realizaremos un cuadrado con turtle

# Turtle es un modulo de Python que nos sirven para generar interfaces graficas
import turtle

# decimos a turtle que queremos generar una ventana
window = turtle.Screen()

# generamos una tortuga llamada david
david = turtle.Turtle()

#generamos lineas para un cuadrado
david.forward(50)
david.left(90)
david.forward(50)
david.left(90)
david.forward(50)
david.left(90)
david.forward(50)
david.left(90)

# diremos que turtle no nos cierre la ventana
turtle.mainloop()
