## Create rectangle modern art

Now let’s create some modern art by drawing lots of rectangles of different sizes and colours. 

--- task ---

First add the following code to the bottom of your script, after your challenge code, to clear the screen after your turtle art and point the turtle in its usual direction:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 33
line_highlights: 33-34
---
clear()
setheading(0)
--- /code ---

--- /task ---

--- task ---

You can comment out your turtle art code by placing a `#` at the beginning of each line so that it doesn’t run while you are working on rectangle art. (Then you can uncomment it later to show off all of your work.)

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
line_highlights: 26-30
---
# for i in range(1, 30):
#     randomcolour()
#     randomplace()
#     randomheading()
#     stamp()
--- /code ---

--- /task ---

 --- task ---
 
Now let’s add a function to draw a random-sized, random-coloured rectangle at a random location! 
    
Add a `drawrectangle()` function **after** your other functions:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 
---
def drawrectangle():
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
--- /code ---
    
Look in `snippets.py` for some helper code if you want to save some typing time.

 --- /task ---

--- task ---

Add the following code at the bottom of `main.py` to call your new function:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 49
line_highlights: 52
---
clear()
setheading(0)

drawrectangle()
--- /code ---
    
Run your script a few times to see the height and width change. 

The rectangle is always the same colour and starts at the same location.
--- /task ---



--- task ---
Now you’ll need to set the turtle to a random colour and then move it to a random place. Hey, didn’t you already create functions to do that? Awesome. You can just call them from the beginning of the drawrectangle function: 
    
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 25, 26
---
def drawrectangle():
    randomcolour()
    randomplace()
    hideturtle()
    length = randint(10, 100)
    height = randint(10, 100)
--- /code ---
    
Wow that was a lot less work, and it’s much easier to read. 

--- /task ---

--- task ---

 Now let's call `drawrectangle()` in a loop to create some cool modern art:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 50
line_highlights: 53
---
clear()
setheading(0)

for i in range(20):
    drawrectangle()
--- /code ---

--- /task ---   

--- task ---

Gosh that was a bit slow wasn’t it! Luckily you can speed the turtle up. 

Find the line where you set the shape to 'turtle' and add the highlighted code:
    
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 42
line_highlights: 43
---
shape("turtle")
speed(0)
--- /code ---
    
`speed(0)` is the fastest or you can use numbers from 1 (slow) to 10 (fast.) Experiment until you find a speed you like. 

--- /task ---
  




