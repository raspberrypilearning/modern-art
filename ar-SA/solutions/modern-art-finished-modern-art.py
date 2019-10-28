#!/bin/python3

from turtle import *
from random import *

def randomcolour():
  ###لا تعلق على السطر في الاسفل اذا لم تكن تستخدم trinket###
  #colormode(255)
  أحمر = randint (0 ، 255)
  الأخضر = randint (0 ، 255)
  الأزرق = randint (0 ، 255)
  color (الأحمر والأخضر والأزرق)

مكان عشوائي ():
  penup ()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def عنوان عشوائي():
  العنوان = randint (0 ، 360)
  setheading (العنوان)

def ارسم مستطيل ():
  لون عشوائي ()
  مكان عشوائي()
  اخفاء السلحفاة ()
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

الشكل("سلحفاة")
السرعة (0)

for i in range(1, 30):
  لون عشوائي ()
  مكان عشوائي()
  عنوان عشوائي()
  stamp()

# التحدي - استخدام built في وظيفة dot

def ارسم دائرة():
  نصف القطر = randint (5 ، 100)
  لون عشوائي ()
  مكان عشوائي()
  dot (نصف القطر)

def ارسم نجمة ():
  لون عشوائي ()
  مكان عشوائي()
  عنوان عشوائي()
  begin_fill()
  حجم = randint (20 ، 100)
  # رسم شكل النجم
  للجانب في المدى (5):
    اليسار (144)
    forward(حجم)

  end_fill()

clear()
setheading(0)

for i in range(20):
  ارسم مستطيل ()

clear()

for i in range(50):
  رسم دائرة()

clear()

for i in range(20):
  ارسم نجمة()
