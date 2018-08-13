#!/bin/python3

from turtle import *
from random import *

def randomcolour():
  colormode(255)
  red = randint(0, 255) #赤
  green = randint(0, 255) #緑
  blue = randint(0, 255) #青
  color(red, green, blue)

def randomplace():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def randomheading():
  heading = randint(0, 360)
  setheading(heading)

def drawrectangle():
  randomcolour()
  randomplace()
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
  randomcolour()
  randomplace()
  randomheading()
  stamp()

# チャレンジ - turtleに含まれているdot関数を使って円を描こう

def drawcircle():
  radius = randint(5, 100)
  randomcolour()
  randomplace()
  dot(radius)

def drawstar():
  randomcolour()
  randomplace()
  randomheading()
  begin_fill()
  size = randint(20, 100)
  #星を描く
  for side in range(5):
    left(144)
    forward(size)

  end_fill()

clear()
setheading(0)

for i in range(20):
  drawrectangle()

clear()

for i in range(50):
  drawcircle()

clear()

for i in range(20):
  drawstar()
