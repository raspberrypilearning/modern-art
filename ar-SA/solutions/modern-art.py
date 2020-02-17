#!/bin/python3

from turtle import *
from random import *

def randomcolour():
  أحمر = randint (0 ، 255)
  أخضر = randint (0 ، 255)
  أزرق = randint (0 ، 255)
  color (أحمر، أخضر، أزرق)

مكان عشوائي():
  penup ()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()
  
def عنوان عشوائي():
  العنوان = randint (0 ، 360)
  setheading (العنوان)

def ارسم مستطيل():
  لون عشوائي()
  مكان عشوائي()
  اخفاء السلحفاة()
  طول = randint (10 ، 100)
  ارتفاع = randint (10 ، 100)
  begin_fill()
  forward (الطول)
  اليمين(90)
  forward (الارتفاع)
  اليمين(90)
  forward (الطول)
  اليمين(90)
  forward (الارتفاع)
  اليمين(90)
  end_fill()
  
الشكل("turtle")
السرعة(0)

for i in range(1, 30):
  لون عشوائي()
  مكان عشوائي()
  عنوان عشوائي()
  stamp()
  
# التحدي - استخدام built في وظيفة dot

def ارسم دائرة():
  نصف القطر = randint (5 ، 100)
  لون عشوائي()
  مكان عشوائي()
  dot (نصف القطر)
  
def ارسم نجمة():
  لون عشوائي()
  مكان عشوائي()
  عنوان عشوائي()
  begin_fill()
  حجم = randint (20 ، 100)
  #ارسم شكل النجمة
  للجانب في المدى (5):
    اليسار(144)
    forward(حجم)

  end_fill()
  
clear()
setheading(0)
  
for i in range(20):
  أرسم مستطيل()
  
clear()
  
for i in range(50):
  أرسم دائرة()

clear()

for i in range(20):
  ارسم نجمة()


