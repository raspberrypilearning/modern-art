## Colores aleatorios

+ Abre este trinket: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ Puedes determinar el color de una tortuga indicando qué tan roja, verde y azul quisieras que sea desde 0 a 255.
    
    Añade el siguiente código para obtener una tortuga morada:
    
    ![captura de pantalla](images/modern-purple.png)
    
    El morado se obtiene mezclando rojo y azul.

## \--- collapse \---

## title: "Error - mala secuencia de colores: (150, 0, 150)"

¿Te aparece el error `mala secuencia de colores: (150, 0, 150)` cuando ejecutas tu código?

Esto se debe a que Trinket usa un modo de color diferente a otros editores Python. Se puede solucionar cambiando el `colormode` a `255`.

```python
from turtle import *

colormode(255)

shape("turtle")
color(150,0,150)
```

\--- /collapse \---

+ Prueba diferentes números para obtener diferentes colores.
    
    Recuerda que cada número puede ser desde 0 a 255.

+ ¿Qué tal si escoges un número al azar?
    
    Actualiza tu código para escoger un número al azar entre 0 y 255 para los valores de rojo, verde y azul:
    
    ![captura de pantalla](images/modern-random-colour.png)

+ Haz click en "Run" un par de veces para obtener tortugas de diferentes colores.

+ Es divertido, pero es demasiado para recordar y escribir cada vez que quieras asignar un color al azar a una tortuga y no es tan fácil de leer.
    
    In Python we can write `def` to define a function that we can call whenever we need to set the turtle to a random colour.
    
    You’ve been calling functions already, `color()` and `randint()` are functions that have been defined for you.
    
    Let’s put the random colour code into a function using def:
    
    ![screenshot](images/modern-colour-function.png)
    
    Make sure you indent the code inside the function. Functions are usually placed at the top of the script after the imports.

+ If you ‘Run’ your code now you don’t get a random coloured turtle. That’s because you have defined your function, but not called it yet.

+ Add a line to call your new function:
    
    ![screenshot](images/modern-call-colour.png)
    
    Notice that your new code is much easier to understand because the complex part is in the function. It’s easy to work out what `randomcolour()` does.