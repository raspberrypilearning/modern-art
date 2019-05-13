## Nasumične boje

+ Otvori sljedeći trinket: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ Možeš da podesiš boju kornjače tako što ćeš odrediti koliko želiš crvene, zelene i plave boje od 0 do 255.
    
    Dodaj sljedeći kôd da tvoja kornjača bude ljubičasta:
    
    ![screenshot](images/modern-purple.png)
    
    Ljubičasta se dobije kada se pomiješaju crvena i plava boja.

\--- collapse \---

* * *

## title: "Error - bad color sequence: (150, 0, 150)"

Do you get the error `bad color sequence: (150, 0, 150)` when running your code.

This is because trinket uses a different colour mode to other Python editors. It can be fixed by changing the `colormode` to `255`.

```python
from turtle import *

colormode(255)

shape("turtle")
color(150,0,150)
```

\--- /collapse \---

+ Try some different numbers to get different colours.
    
    Remember each number can be from 0 to 255.

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