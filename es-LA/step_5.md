## Crea arte moderno rectangular

Ahora vamos a crear arte moderno dibujando varios rectángulos de diferentes tamaños y colores.

+ En primer lugar, añade el siguiente código después del código del desafío para limpiar la pantalla después de crear tu arte con tortugas y para que la tortuga apunte en su dirección habitual:
    
    ![captura de pantalla](images/modern-reset.png)

+ Puedes comentar en tu arte con tortugas colocando un `#` al inicio de cada línea para que no se ejecute cuando trabajes en tu arte rectangular. (Puedes quitar estos comentarios luego para mostrar todo tu trabajo)
    
    ![captura de pantalla](images/modern-comment.png)

+ ¡Vamos a añadir una función para dibujar un rectángulo de tamaño y color aleatorio en una ubicación aleatoria!
    
    Añade una función `drawrectangle()` después de las funciones que ya has añadido:
    
    ![captura de pantalla](images/modern-rect-function.png)
    
    Busca en `snippets.py` para hallar código de ayuda si quieres ahorrarte tiempo tecleando.

+ Añade el siguiente código al final de `main.py` para llamar a tu nueva función:
    
    ![captura de pantalla](images/modern-call-rect.png)
    
    Ejecuta tu código unas cuantas veces para mirar el cambio en el largo y ancho.

+ El rectángulo tiene siempre el mismo color y empieza en el mismo lugar.
    
    Ahora tendrás que definir un color aleatorio para la tortuga y, luego, moverla a un lugar aleatorio. Pero... ¿no habías creado antes funciones para hacer eso? ¡Genial! Tan solo puedes llamarlas desde el comienzo de la función drawrectangle:
    
    ![captura de pantalla](images/modern-random-rect.png)
    
    ¡Bien! Nos ahorramos bastante trabajo y ahora es mucho más fácil de leer.

+ Ahora, llamemos `drawrectangle()` en un bucle para crear arte moderno alucinante:
    
    ![captura de pantalla](images/modern-rect-art.png)

+ Vaya, eso fue algo lento, ¿verdad? Afortunadamente, puedes hacer que la tortuga vaya más rápido.
    
    Encuentra la línea donde fijas la forma de "tortuga" y añade el código resaltado:
    
    ![captura de pantalla](images/modern-speed.png)
    
    `speed(0)` es el más rápido, o puedes usar números desde el 1 (lento) al 10 (rápido). Experimenta hasta que encuentres tu velocidad preferida.