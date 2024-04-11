## Random colours

Open the [Modern Art starter](https://editor.raspberrypi.org/en/projects/modern-art-starter){:target="_blank"} project. The code editor will open in another browser tab.

--- task ---
You can set the colour of a turtle by saying how much red, green and blue you would like from 0 to 255. 

Add the following code to get a purple turtle:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 3-6
---
from turtle import *

colormode(255)

shape("turtle")
color(150, 0, 150)

--- /code ---
   
Purple is made by mixing together red and blue.

--- /task ---

--- task ---

Try some different numbers to get different colours. 

Remember each number can be from 0 to 255. 

--- /task ---

--- task ---

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 3-6
---
from turtle import *
from random import *

colormode(255)

shape("turtle")
color(150, 0, 150)

--- /code ---

--- /task ---

+ How about choosing a random colour?

    Update your code to choose a random number between 0 and 255 for the red, green and blue values:
    
    ![screenshot](images/modern-random-colour.png)

+ Click ‘Run’ a few times to get different coloured turtles.

+ That’s fun, but it’s a lot to remember and type every time you want to set a turtle to a random colour and it’s not very easy to read. 

    In Python we can write `def` to define a function that we can call whenever we need to set the turtle to a random colour. 

    You’ve been calling functions already, `color()` and `randint()` are functions that have been defined for you. 

    Let’s put the random colour code into a function using def:
  
    ![screenshot](images/modern-colour-function.png)
    
  Make sure you indent the code inside the function. Functions are usually placed at the top of the script after the imports. 
  
+ If you ‘Run’ your code now you don’t get a random coloured turtle. That’s because you have defined your function, but not called it yet. 
  
+ Add a line to call your new function:
  
    ![screenshot](images/modern-call-colour.png)

    Notice that your new code is much easier to understand because the complex part is in the function. It’s easy to work out what `randomcolour()` does.

