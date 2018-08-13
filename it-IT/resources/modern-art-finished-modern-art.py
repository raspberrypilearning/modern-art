#!/bin/python3

from turtle import *
from random import *

def colorecasuale():
  colormode(255)
  rosso = randint(0, 255)
  verde = randint(0, 255)
  blu = randint(0, 255)
  color(rosso, verde, blu)

def posizionecasuale():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def direzionecasuale():
  direzione = randint(0, 360)
  setheading(direzione)

def disegnarettangolo():
  colorecasuale()
  posizionecasuale()
  hideturtle()
  base = randint(10, 100)
  altezza = randint(10, 100)
  begin_fill()
  forward(base)
  right(90)
  forward(altezza)
  right(90)
  forward(base)
  right(90)
  forward(altezza)
  right(90)
  end_fill()

shape("turtle")
speed(0)

for i in range(1, 30):
  colorecasuale()
  posizionecasuale()
  direzionecasuale()
  stamp()

# Sfida - usa la funzione punto incorporata

def disegnacerchio():
  raggio = randint(5, 100)
  colorecasuale()
  posizionecasuale()
  dot(raggio)

def disegnastella():
  colorecasuale()
  posizionecasuale()
  direzionecasuale()
  begin_fill()
  dimensione = randint(20, 100)
  #disegna una stella
  for lato in range(5):
    left(144)
    forward(dimensione)

  end_fill()

clear()
setheading(0)

for i in range(20):
  disegnarettangolo()

clear()

for i in range(50):
  disegnacerchio()

clear()

for i in range(20):
  disegnastella()
