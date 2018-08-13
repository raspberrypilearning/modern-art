#!/bin/python3

# Code voor het tekenen van een rechthoek met willekeurige grootte
  hideturtle()
  lengte = randint(10, 100)
  hoogte = randint(10, 100)
  begin_fill()
  forward(lengte)
  right(90)
  forward(hoogte)
  right(90)
  forward(lengte)
  right(90)
  forward(hoogte)
  right(90)
  end_fill()
  
# Code om een ​​ster te tekenen
  begin_fill()
  for zijden in range(5):
    left(144)
    forward(50)
  end_fill()
  