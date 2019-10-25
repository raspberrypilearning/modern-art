#!/bin/python3

# Kod do narysowania prostokąta o losowej wielkości
  hideturtle()
  dlugosc = randint(10, 100)
  wysokosc = randint(10, 100)
  begin_fill()
  forward(dlugosc)
  right(90)
  forward(wysokosc)
  right(90)
  forward(dlugosc)
  right(90)
  forward(wysokosc)
  right(90)
  end_fill()
  
# Kod do rysowania gwiazdy
  begin_fill()
  for brzeg in range(5):
    left(144)
    forward(50)
  end_fill()
  