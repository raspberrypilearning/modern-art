#!/bin/python3

from turtle import *
from random import *

def color_aleatorio():
  rojo = randint(0, 255)
  verde = randint(0, 255)
  azul = randint(0, 255)
  color(rojo, verde, azul)

def lugar_aleatorio():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()
  
def rumbo_aleatorio():
  rumbo = randint(0, 360)
  setheading(rumbo)

def dibujar_rectangulo():
  color_aleatorio()
  lugar_aleatorio()
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
  
shape("turtle")
speed(0)

for i in range(1, 30):
  color_aleatorio()
  lugar_aleatorio()
  rumbo_aleatorio()
  stamp()
  
# Desafío - usa la función incorporada dot

def dibujar_circulo():
  radio = randint(5, 100)
  color_aleatorio()
  lugar_aleatorio()
  dot(radio)
  
def dibujar_estrella():
  color_aleatorio()
  lugar_aleatorio()
  rumbo_aleatorio()
  begin_fill()
  tamano = randint(20, 100)
  #dibuja la forma de la estrella
  for lado in range(5):
    left(144)
    forward(tamano)

  end_fill()
  
clear()
setheading(0)
  
for i in range(20):
  dibujar_rectangulo()
  
clear()
  
for i in range(50):
  dibujar_circulo()

clear()

for i in range(20):
  dibujar_estrella()


