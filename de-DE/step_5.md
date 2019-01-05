## Moderne Kunst aus Rechtecken erstellen

Lass uns nun einige moderne Kunstwerke erstellen, indem du viele Rechtecke in verschiedenen Größen und Farben zeichnest.

+ Zuerst fügst du den folgenden Code nach dem Challenge-Code am Ende deines Skripts ein, um den Bildschirm nach deiner Schildkröten-Kunst zu löschen und die Schildkröte in ihre normale Richtung zu weisen:
    
    ![screenshot](images/modern-reset.png)

+ You can comment out your turtle art code by placing a `#` at the beginning of each line so that it doesn’t run while you are working on rectangle art. (Then you can uncomment it later to show off all of your work.)
    
    ![screenshot](images/modern-comment.png)

+ Now let’s add a function to draw a random-sized, random-coloured rectangle at a random location!
    
    Add a `drawrectangle()` function after your other functions:
    
    ![screenshot](images/modern-rect-function.png)
    
    Look in `snippets.py` for some helper code if you want to save some typing time.

+ Add the following code at the bottom of `main.py` to call your new function:
    
    ![screenshot](images/modern-call-rect.png)
    
    Run your script a few times to see the height and width change.

+ The rectangle is always the same colour and starts at the same location.
    
    Now you’ll need to set the turtle to a random colour and then move it to a random place. Hey, didn’t you already create functions to do that? Awesome. You can just call them from the beginning of the drawrectangle function:
    
    ![screenshot](images/modern-random-rect.png)
    
    Wow that was a lot less work, and it’s much easier to read.

+ Now let's call `drawrectangle()` in a loop to create some cool modern art:
    
    ![screenshot](images/modern-rect-art.png)

+ Gosh that was a bit slow wasn’t it! Luckily you can speed the turtle up.
    
    Find the line where you set the shape to 'turtle' and add the highlighted code:
    
    ![screenshot](images/modern-speed.png)
    
    `speed(0)` is the fastest or you can use numbers from 1 (slow) to 10 (fast.) Experiment until you find a speed you like.