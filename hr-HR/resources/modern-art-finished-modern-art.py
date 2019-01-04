#!/bin/python3

from turtle import *
from random import *

def nasumicnaBoja():
  ###Uncomment the line below if you are not using trinket###
  #colormode(255)
  crvena = randint(0, 255)
  zelena = randint(0, 255)
  plava = randint(0, 255)
  color(crvena, zelena, plava)

def nasumicnaPozicija():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def nasumicanSmjer():
  smjer = randint(0, 360)
  setheading(smjer)

def crtajPravokutnik():
  nasumicnaBoja()
  nasumicnaPozicija()
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
  nasumicnaBoja()
  nasumicnaPozicija()
  nasumicanSmjer()
  stamp()

# Izazov - koristi ugrađenu dot funkciju

def crtajKruznicu():
  polumjer = randint(5, 100)
  nasumicnaBoja()
  nasumicnaPozicija()
  dot(polumjer)

def crtajZvijezdu():
  nasumicnaBoja()
  nasumicnaPozicija()
  nasumicanSmjer()
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
  crtajPravokutnik()

clear()

for i in range(50):
  crtajKruznicu()

clear()

for i in range(20):
  crtajZvijezdu()
