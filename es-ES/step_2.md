## Colores aleatorios

+ Abre este Trinket: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/codecraft-go</a>.

+ Puedes definir el color de la tortuga diciendo cuánto rojo, verde y azul te gustaría que tuviera, del 0 al 255.
    
    Añade el siguiente código para obtener una tortuga violeta:
    
    ![screenshot](images/modern-purple.png)
    
    El violeta se hace mezclando el rojo y el azul.

+ Prueba con números diferentes para obtener diferentes colores.
    
    Recuerda que cada número puede ser del 0 al 255.

+ ¿Y si elegimos un color alelatorio?
    
    Actualiza el código para elegir un número aleatorio entre 0 y 255 para los valores rojo, verde y azul:
    
    ![screenshot](images/modern-random-colour.png)

+ Haz clic en 'Run varias veces para obtener tortugas de diferentes colores.

+ Es divertido! Pero es mucho para recordar y escribir cada vez que quieres asignarle a la tortuga un color aleatorio, y no es muy fácil de leer.
    
    En Python podemos escribir `def` para definir una función a la que podamos llamar cada vez que necesitemos asignar a la tortuga un color aleatorio.
    
    Ya has estado haciendo llamadas a funciones, `color()` y `randint()` son funciones que vienen predefinidas.
    
    Vamos a poner en una función el código para el color aleatorio usando def:
    
    ![screenshot](images/modern-colour-function.png)
    
    Asegúrate de indentar el código dentro de la función. Las funciones generalmente se colocan en la parte superior del script, justo después de los import.

+ Si ejecutas el código ahora con 'Run', no obtendrás una tortuga de color aleatorio. Eso se debe a que has definido su función, pero aún no la has llamado.

+ Añade una línea para llamar a tu nueva función:
    
    ![screenshot](images/modern-call-colour.png)
    
    Observa que el nuevo código es mucho más fácil de entender porque la parte compleja se encuentra en la función. Es fácil entender qué hace `randomcolour()`.