#!/bin/python3

from turtle import *
from random import *

def willekeurigekleur():
  colormode(255)
  rood = randint(0, 255)
  groen = randint(0, 255)
  blauw = randint(0, 255)
  color(rood, groen, blauw)

def willekeurigeplek():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def willekeurigerichting():
  richting = randint(0, 360)
  setheading(richting)

def tekenrechthoek():
  willekeurigekleur()
  willekeurigeplek()
  hideturtle()
  lengte = randint(10, 100)
  hoogte = randint(10, 100)
  begin_fill()
  forward(lengte)
  right(90)
  forward(hoogte)
  right(90)
  forward(lengte)
  right(90)
  forward(hoogte)
  right(90)
  end_fill()

shape("turtle")
speed(0)

for i in range(1, 30):
  willekeurigekleur()
  willekeurigeplek()
  willekeurigerichting()
  stamp()

# Uitdaging - gebruik ingebouwde dot functie

def tekencirkel():
  radius = randint(5, 100)
  willekeurigekleur()
  willekeurigeplek()
  dot(radius)

def tekenster():
  willekeurigekleur()
  willekeurigeplek()
  willekeurigerichting()
  begin_fill()
  grootte = randint(20, 100)
  #teken de ster vorm
  for zijden in range(5):
    left(144)
    forward(grootte)

  end_fill()

clear()
setheading(0)

for i in range(20):
  tekenrechthoek()

clear()

for i in range(50):
  tekencirkel()

clear()

for i in range(20):
  tekenster()
