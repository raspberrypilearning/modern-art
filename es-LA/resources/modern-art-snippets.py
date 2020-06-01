#!/bin/python3

# Código para dibujar un rectángulo de tamaño aleatorio
  hideturtle()
  ancho = randint(10, 100)
  alto = randint(10, 100)
  begin_fill()
  forward(ancho)
  right(90)
  forward(alto)
  right(90)
  forward(ancho)
  right(90)
  forward(alto)
  right(90)
  end_fill()
  
# Código para dibujar una estrella
  begin_fill()
  for lado in range(5):
    left(144)
    forward(50)
  end_fill()
  