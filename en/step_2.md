## Random colours

--- task ---
Open the [Modern Art starter project](https://editor.raspberrypi.org/en/projects/modern-art-starter){:target="_blank"}. 
--- /task ---

Colours of light are made of red, green and blue. Set a colour by saying how much red, green and blue you would like, from 0 to 255. 


--- task ---
Add the following code to get a red turtle:

--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 5-6
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
line_number_start: 5
line_highlights: 5-8
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

Put the random colour code into a function by adding a `def` with a name, and then indenting it.

--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 5-9
---
def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)

shape("turtle")
--- /code ---
--- /task ---

--- task ---
Click **Run**. You won't see a random coloured turtle because you have defined your function, but not called it yet. 
--- /task ---

--- task ---
Add a line to call your new function:
  
--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 11
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

Notice that your new code is much easier to understand because the complex part is in the function. It’s easy to work out what `randomcolour()` does.

  


