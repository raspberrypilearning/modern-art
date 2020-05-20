## Crea arte moderno rectangular

Ahora vamos a crear arte moderno dibujando muchos rectángulos de diferentes tamaños y colores.

+ En primer lugar, añade el siguiente código después del código del desafío para limpiar la pantalla después de crear tu arte con tortugas y para que la tortuga apunte en su dirección habitual:
    
    ![captura de pantalla](images/modern-reset.png)

+ Puedes comentar el código de "arte con tortugas" colocando un `#` al comienzo de cada línea para que esa línea no se ejecute mientras trabajas en tu "creación de arte rectangular". (Puedes descomentarlo más tarde para mostrar todo tu trabajo).
    
    ![captura de pantalla](images/modern-comment.png)

+ ¡Vamos a añadir una función para dibujar un rectángulo de tamaño aleatorio de color aleatorio y en una ubicación aleatoria!
    
    Añade la función `drawrectangle()` después de las funciones que ya has añadido:
    
    ![captura de pantalla](images/modern-rect-function.png)
    
    Investiga en `snippets.py` para hallar código de ayuda si quieres ahorrarte tiempo tecleando.

+ Añade el siguiente código en la parte inferior de `main.py` para llamar a la nueva función:
    
    ![captura de pantalla](images/modern-call-rect.png)
    
    Ejecute su script unas cuantas veces para ver el cambio de altura y ancho.

+ El rectángulo siempre tiene el mismo color y se sitúa en la misma ubicación.
    
    Ahora tendrás que definir un color aleatorio para la tortuga y, a continuación, moverla a un lugar aleatorio. Pero... ¿no has creado antes funciones para hacer eso? ¡Genial! Puedes llamar las desde el comienzo de la función drawrectangle:
    
    ![captura de pantalla](images/modern-random-rect.png)
    
    ¡Muy bien! Nos hemos ahorrado trabajo y es mucho más fácil de leer.

+ Vamos a llamar a `drawrectangle()` en un bucle para crear arte moderno alucinante:
    
    ![captura de pantalla](images/modern-rect-art.png)

+ Caramba, es un poco lento, ¿no? Afortunadamente puedes hacer que la tortuga vaya más rápido.
    
    Encuentra la línea donde das forma de tortuga -shape("turtle")- y añade el código resaltado:
    
    ![captura de pantalla](images/modern-speed.png)
    
    `speed(0)` es la velocidad más rápida. Puedes usar los números del 1 (lento) al 10 (rápido). Haz pruebas hasta encontrar la velocidad que te guste.