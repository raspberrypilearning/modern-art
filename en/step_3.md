## Random place

Now that you know how to create a function, let’s create another function to move the turtle to a random place on the screen. 

The centre of the screen is at coordinates (0,0). 

--- task ---

Add a `randomplace()` function which chooses a random x, y coordinate and moves the turtle to that coordinate.

--- code ---
---
language: python
line_numbers: true
line_number_start: 6
line_highlights: 12-15
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

Add code to call your function, then click **Run**.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 18
---
def randomplace():
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)

randomcolour()
randomplace()
shape("turtle")

--- /code ---
--- /task ---
    
Ooops, the cursor starts as an arrow and draws when it moves!

--- task ---
To fix this:
+ Put the pen up at the beginning and down at the end so that the turtle doesn’t draw while it’s moving.
+ Set the turtle shape before you begin moving or selecting colours.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 13, 17, 19
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

--- /code ---

--- /task ---
 
--- task ---

Now click **Run** a few times to check that your turtle appears in a random place with a random colour.

--- /task ---

