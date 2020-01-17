#!/bin/python3

# 绘制随机大小矩形的代码
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
  
# 绘制星星的代码
  begin_fill()
  for side in range(5):
    left(144)
    forward(50)
  end_fill()
  