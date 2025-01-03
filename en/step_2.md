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
shape("turtle")
color(255, 0, 0)
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
line_highlights: 6-9
---
shape("turtle")
red = randint(0, 255)
green = randint(0, 255)
blue = randint(0, 255)
color(red, green, blue)
--- /code ---
--- /task ---

--- task ---
Click **Stop** then click **Run** a few times to get different coloured turtles.
--- /task ---



That’s fun, but it’s a lot to remember and type every time you want to set a turtle to a random colour and it’s not very easy to read. 

In Python we can write `def` to give this section of code a name that we can use to run it whenever we need to set the turtle to a random colour. 


--- task ---

Put the random colour code into a function using def:

--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 5-11
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
Click **Stop** then **Run**. You won't see a random coloured turtle because you have defined your function, but not called it yet. 
--- /task ---

--- task ---
Add a line to call your new function:
  
--- code ---
---
language: python
line_numbers: true
line_number_start: 5
line_highlights: 12
---
def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)

shape("turtle")
randomcolour()
--- /code ---
--- /task ---

Notice that your new code is much easier to understand because the complex part is in the function. It’s easy to work out what `randomcolour()` does.

  


