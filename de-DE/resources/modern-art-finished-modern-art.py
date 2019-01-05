#!/bin/python3

from turtle import *
from random import *

def zufallsfarbe():
  ###Entferne das Kommentarzeichen in der nächsten Zeile, wenn du nicht mit Trinket arbeitest###
  #colormode(255)
  rot = randint(0, 255)
  gruen = randint(0, 255)
  blau = randint(0, 255)
  color(rot, gruen, blau)

def zufallsort():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def zufallstitel():
  richtung = randint(0, 360)
  setheading(richtung)

def zeichnerechteck():
  zufallsfarbe()
  zufallsort()
  hideturtle()
  laenge = randint(10, 100)
  hoehe = randint(10, 100)
  begin_fill()
  forward(laenge)
  right(90)
  forward(hoehe)
  right(90)
  forward(laenge)
  right(90)
  forward(hoehe)
  right(90)
  end_fill()

shape("turtle")
speed(0)

for i in range(1, 30):
  zufallsfarbe()
  zufallsort()
  zufallstitel()
  stamp()

# Aufgabe - verwende die eingebaute dot-Funktion

def zeichnekreis():
  radius = randint(5, 100)
  zufallsfarbe()
  zufallsort()
  dot(radius)

def zeichnestern():
  zufallsfarbe()
  zufallsort()
  zufallstitel()
  begin_fill()
  groesse = randint(20, 100)
  #zeichne den Stern
  for side in range(5):
    left(144)
    forward(groesse)

  end_fill()

clear()
setheading(0)

for i in range(20):
  zeichnerechteck()

clear()

for i in range(50):
  zeichnekreis()

clear()

for i in range(20):
  zeichnestern()
