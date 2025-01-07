## Random colours

--- task ---
Open the [Modern Art starter project](https://editor.raspberrypi.org/en/projects/modern-art-starter){:target="_blank"}. 
--- /task ---

Colours can be created by mixing red, green and blue. 

Create a colour by setting how much red, green and blue you would like, from 0 to 255. 


--- task ---
Add the following code to get a red turtle:

--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 6-7
---
color(255, 0, 0)
shape("turtle")
--- /code ---

--- /task ---

--- task ---
Click **Run** to see your red turtle.
--- /task ---

--- task ---
Try changing the numbers to get different colours. Remember each number can be from 0 to 255. 
--- /task ---

How about choosing a random colour?

--- task ---
Update your code to choose a random number between 0 and 255 for the red, green and blue values:

--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 6-9
---
red = randint(0, 255)
green = randint(0, 255)
blue = randint(0, 255)
color(red, green, blue)
shape("turtle")
--- /code ---
--- /task ---

--- task ---
Click **Run** a few times to see different coloured turtles.
--- /task ---


That’s fun, but it’s a lot to remember and type every time you want to set a turtle to a random colour and it’s not very easy to read. 

In Python you can give this section of code a name, and then run it whenever you want to set the turtle to a random colour. This is called a **function**.

--- task ---

Put the random colour code into a function by adding a `def` with a name to **def**ine a function, and then indenting the code within it.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 6-10
---
from turtle import *
from random import *

colormode(255)

def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)

shape("turtle")
--- /code ---
--- /task ---

--- task ---
Click **Run**. The turtle will always be black, because you have defined your `randomcolour()` function, but not called it yet. 
--- /task ---

--- task ---
Add a line to call your new function:
  
--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 12
---
def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)

randomcolour()
shape("turtle")
--- /code ---
--- /task ---

--- task ---
Click **Run** a few times and test that your turtle is a random colour again. 
--- /task ---


