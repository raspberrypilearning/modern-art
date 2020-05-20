#!/bin/python3

# Código para desenhar um retângulo de tamanho aleatório
  hideturtle()
  comprimento = randint(10, 100)
  altura = randint(10, 100)
  begin_fill()
  forward(comprimento)
  right(90)
  forward(altura)
  right(90)
  forward(altura)
  right(90)
  forward(altura)
  right(90)
  end_fill()
  
# Código para desenhar uma estrela
  begin_fill()
  for lado in range(5):
    left(144)
    forward(50)
  end_fill()
  