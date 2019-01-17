#!/bin/python3

# Code um ein zufällig großes Rechteck zu zeichnen
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
  
# Code um einen Stern zu zeichnen
  begin_fill()
  for seiten in range(5):
    left(144)
    forward(50)
  end_fill()
  