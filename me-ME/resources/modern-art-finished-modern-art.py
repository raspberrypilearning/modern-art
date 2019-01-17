#!/bin/python3

from turtle import *
from random import *

def nasumicnaboja():
  ###Ukloni znak # u redu ispod ako ne koristiš trinket###
  #colormode(255)
  crvena = randint(0, 255)
  zelena = randint(0, 255)
  plava = randint(0, 255)
  color(crvena, zelena, plava)

def nasumicnapozicija():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def nasumicansmjer():
  smjer = randint(0, 360)
  setheading(smjer)

def crtajpravougaonik():
  nasumicnaboja()
  nasumicnapozicija()
  hideturtle()
  duzina = randint(10, 100)
  visina = randint(10, 100)
  begin_fill()
  forward(duzina)
  right(90)
  forward(visina)
  right(90)
  forward(duzina)
  right(90)
  forward(visina)
  right(90)
  end_fill()

shape("turtle")
speed(0)

for i in range(1, 30):
  nasumicnaboja()
  nasumicnapozicija()
  nasumicansmjer()
  stamp()

# Izazov - koristi ugrađenu dot funkciju

def crtajkrug():
  poluprecnik = randint(5, 100)
  nasumicnaboja()
  nasumicnapozicija()
  dot(poluprecnik)

def crtajzvijezdu():
  nasumicnaboja()
  nasumicnapozicija()
  nasumicansmjer()
  begin_fill()
  velicina = randint(20, 100)
  #nacrtaj oblik zvijezde
  for stranica in range(5):
    left(144)
    forward(velicina)

  end_fill()

clear()
setheading(0)

for i in range(20):
  crtajpravougaonik()

clear()

for i in range(50):
  crtajkrug()

clear()

for i in range(20):
  crtajzvijezdu()
