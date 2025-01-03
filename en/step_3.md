## Random place

Let’s create another function to move the turtle to a random place on the screen. The center of the screen is (0,0) so we’ll place turtles in a square area around the centre. 

--- task ---

Add a `randomplace()` function:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 14-17
---
def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)


def randomplace():
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
--- /code ---

--- /task ---

--- task ---

Try your new function by calling it and then calling `stamp()`, you can call it more than once:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14
line_highlights: 22-26
---
def randomplace():
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)


shape("turtle")
randomcolour()
randomplace()
stamp()
randomcolour()
randomplace()
stamp()
--- /code ---

--- /task ---
    
--- task ---

Ooops, the turtle draws when it moves. Let’s put the pen up at the beginning and down at the end so that the turtle doesn’t draw while it’s moving:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 14
line_highlights: 15, 19
---
def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()


shape("turtle")
randomcolour()
randomplace()
stamp()
randomcolour()
randomplace()
stamp()
--- /code ---

Did you notice that you only had to 'fix' the code in one place? That's another good thing about functions. 

--- /task ---
 
--- task ---

Now test your code a few times.

--- /task ---

