#!/bin/python3

거북이를 불러들이세요
랜덤(무작위 추첨) 을 불러들이세요

def randomcolour():
  ###trinket를 사용하지 않고 있다면 아래의 줄을 주석 해제하세요.(주석은 메모를 의미합니다)###
  #colormode(255)
  red = randint(0, 255)
  green = randint(0, 255)
  blue = randint(0, 255)
  color(red, green, blue)

def randomplace():
  펜을 올리세요()
  x = randint(-100, 100)
  y = randint(-100, 100)
  (x,y)로 가라
  펜 내리기()

향할 곳을 랜덤으로 지정():
  향하는 곳 = randint(0, 360)
  제목 (제목)

직각삼각형 그리기를 정의():
  랜덤색상()
  랜덤장소()
  거북이 숨기기()
  길이 = randit(10,100)
  높이(세로) = randint(10, 100)
  채우기_시작()
  앞으로 (길이)
  오른쪽 (90)
  앞으로 (높이)
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

# Challenge - use built in dot function

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
  #draw the star shape
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
