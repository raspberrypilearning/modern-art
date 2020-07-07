#!/bin/python3

# ये कोड एक random आकार के रेक्टेंगल (rectangle) बनाने के लिए हैं
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
  
# स्टार बनाने के लिए कोड
  begin_fill()
  for side in range(5):
    left(144)
    forward(50)
  end_fill()
  