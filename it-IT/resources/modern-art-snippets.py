#!/bin/python3

# Codice per disegnare un rettangolo di dimensioni casuali
  hideturtle()
  base = randint(10, 100)
  altezza = randint(10, 100)
  begin_fill()
  forward(base)
  right(90)
  forward(altezza)
  right(90)
  forward(base)
  right(90)
  forward(altezza)
  right(90)
  end_fill()
  
# Codice per disegnare una stella
  begin_fill()
  for lato in range(5):
    left(144)
    forward(50)
  end_fill()
  