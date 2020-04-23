#!/bin/python3

# 무작위 크기의 직사각형을 그리는 코드
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
  
# 별을 그리는 코드
  begin_fill()
  for side in range(5):
    left(144)
    forward(50)
  end_fill()
  