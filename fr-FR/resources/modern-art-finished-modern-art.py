#!/bin/python3

from turtle import *
from random import *

def couleuraleatoire():
  ###Décommente la ligne ci-dessous si tu n'utilises pas trinket###
  #colormode(255)
  red = randint(0, 255)
  green = randint(0, 255)
  blue = randint(0, 255)
  color(red, green, blue)

def endroitaleatoire():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def directionaleatoire():
  heading = randint(0, 360)
  setheading(heading)

def dessinerrectangle():
  couleuraleatoire()
  endroitaleatoire()
  hideturtle()
  length = randint(10, 100)
  height = randint(10, 100)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  forward(height)
  right(90)
  end_fill()

shape("turtle")
speed(0)

for i in range(1, 30):
  couleuraleatoire()
  endroitaleatoire()
  directionaleatoire()
  stamp()

# Défi - utiliser la fonction dot

def dessinercercle():
  radius = randint(5, 100)
  couleuraleatoire()
  endroitaleatoire()
  dot(radius)

def dessineretoile():
  couleuraleatoire()
  endroitaleatoire()
  directionaleatoire()
  begin_fill()
  size = randint(20, 100)
  #dessiner la forme de l'étoile
  for side in range(5):
    left(144)
    forward(size)

  end_fill()

clear()
setheading(0)

for i in range(20):
  dessinerrectangle()

clear()

for i in range(50):
  dessinercercle()

clear()

for i in range(20):
  dessineretoile()
