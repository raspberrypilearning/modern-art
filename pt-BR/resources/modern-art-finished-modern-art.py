#!/bin/python3

from turtle import *
from random import *

def coraleatoria ():
  ###Uncomment the line below if you are not using trinket###
  #colormode(255)
  vermelho = randint(0, 255)
  verde = randint(0, 255)
  azul = randint(0, 255)
  color(vermelho, verde, azul)

def lugaraleatorio():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def irparaaleatorio():
  irpara = randint(0, 360)
  setheading(irpara)

def desenharetangulo():
  coraleatoria()
  lugaraleatorio()
  hideturtle()
  comprimento = randint(10, 100)
  altura = randint(10, 100)
  begin_fill()
  forward(comprimento)
  right(90)
  forward(altura)
  right(90)
  forward(comprimento)
  right(90)
  forward(altura)
  right(90)
  end_fill()

shape("turtle")
speed(0)

for i in range(1, 30):
  coraleatoria()
  lugaraleatorio()
  irparaaleatorio()
  stamp()

# Desafio - use a função de ponto embutido

def desenhacirculo():
  raio = randint(5, 100)
  coraleatoria()
  lugaraleatorio()
  dot(raio)

def desenhaestrela():
  coraleatoria()
  lugaraleatorio()
  irparaaleatorio()
  begin_fill()
  tamanho = randint(20, 100)
  #desenhar a forma de estrela
  for lado in range(5):
    left(144)
    forward(tamanho)

  end_fill()

clear()
setheading(0)

for i in range(20):
  desenharetangulo()

clear()

for i in range(50):
  desenhacirculo()

clear()

for i in range(20):
  desenhaestrela()
