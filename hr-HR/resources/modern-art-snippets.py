#!/bin/python3

# Kôd za crtanje pravokutnika nasumične veličine
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
  
# Kôd za crtanje zvijezde
  begin_fill()
  for stranica in range(5):
    left(144)
    forward(50)
  end_fill()
  