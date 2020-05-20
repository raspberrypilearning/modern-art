#!/bin/python3

from turtle import *
from random import *

def coraleatoria():
  ###remova o comentário da linha abaixo se você não estiver usando o trinket###
  #colormode(255)
  vermelha = randint(0, 255)
  verde = randint(0, 255)
  azul = randint(0, 255)
  color(vermelha, verde, azul)

def lugaraleatorio():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def posicaoaleatoria():
  posicao = randint(0, 360)
  setheading(posicao)

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
  posicaoaleatoria()
  stamp()

# Desafio - use a função embutida dot

def desenhacirculo():
  raio = randint(5, 100)
  coraleatoria()
  lugaraleatorio()
  dot(raio)

def desenhaestrela():
  coraleatoria()
  lugaraleatorio()
  posicaoaleatoria()
  begin_fill()
  tamanho = randint(20, 100)
  #desenha a forma de uma estrela
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
