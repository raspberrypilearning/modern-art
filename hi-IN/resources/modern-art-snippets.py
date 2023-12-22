#!/bin/python3

#यह कोड एक यादृच्छिक आकर का रेक्टेंगल बनाने के लिए है
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
  
#तारा बनाने के लिए कोड
  begin_fill()
  for side in range(5):
    left(144)
    forward(50)
  end_fill()
  