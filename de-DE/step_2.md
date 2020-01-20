## Zufällige Farben

+ Öffne diesen Trinket: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ Du kannst die Farbe einer Schildkröte einstellen, indem du Rot, Grün und Blau mischt, jeweils mit Werten zwischen 0 und 255.
    
    Füge den folgenden Code hinzu, um eine lila Schildkröte zu erhalten:
    
    ![Screenshot](images/modern-purple.png)
    
    Lila wird durch Mischen von Rot und Blau hergestellt.

## \--- collapse \---

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

+ Probiere verschiedene Zahlen aus, um andere Farben zu erhalten.
    
    Denke daran, dass jede Zahl zwischen 0 und 255 liegen kann.

+ Wie wäre es mit einer zufälligen Farbe?
    
    Aktualisiere deinen Code, um eine Zufallszahl zwischen 0 und 255 für die roten, grünen und blauen Werte auszuwählen:
    
    ![Bildschirmfoto](images/modern-random-colour.png)

+ Klicke ein paar Mal auf "Run", um verschiedenfarbige Schildkröten zu erhalten.

+ Das macht Spaß, aber du musst dir viel merken und tippen, wenn du eine Schildkröte auf eine zufällige Farbe setzen möchtest. Außerdem ist es nicht sehr einfach zu lesen.
    
    In Python können wir `def` schreiben um eine Funktion zu definieren, die wir jedesmal aufrufen können, wenn wir die Schildkröte auf eine zufällige Farbe setzen müssen.
    
    Du hast bereits Funktionen aufgerufen, `color()` und `randint()` sind Funktionen, die für dich definiert wurden.
    
    Machen wir mit def aus dem Code für eine zufällige Farbe eine Funktion:
    
    ![Bildschirmfoto](images/modern-colour-function.png)
    
    Stelle sicher, dass du den Code innerhalb der Funktion einrückst. Funktionen werden normalerweise nach den Importen an den Anfang des Skripts gestellt.

+ Wenn du deinen Code jetzt mit "Run" ausführst, erhältst du keine zufällig gefärbte Schildkröte. Das liegt daran, dass du deine Funktion zwar definiert hast, sie aber noch nicht aufgerufen hast.

+ Füge eine Zeile hinzu, um deine neue Funktion aufzurufen:
    
    ![Bildschirmfoto](images/modern-call-colour.png)
    
    Beachte, dass dein neuer Code viel einfacher zu verstehen ist, da sich der komplexe Teil in der Funktion befindet. Es ist leicht herauszufinden, was `zufallsfarbe()` macht.