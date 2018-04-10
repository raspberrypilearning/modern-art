## Colores aleatorios

+ Abre este trinket: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>. 

+ Puedes ajustar el color de una tortuga indicando la cantidad de rojo, verde y azul deseada de 0 a 255. 

    Añade el siguiente código para obtener una tortuga púrpura.

    ![screenshot](images/modern-purple.png)
   
    El color púrpura se logra mezclando el color rojo y el color azul.

+ Prueba con números distintos para lograr colores diferentes. 

    Recuerda que cada número puede ajustarse entre 0 y 255. 

+ ¿Por qué no intentar seleccionar un color aleatorio?

    Actualiza tu código de modo que seleccione un número aleatorio entre 0 y 255 para los valores del color rojo, verde y azul:
    
    ![screenshot](images/modern-random-colour.png)

+ Haz clic en 'Run' varias veces para obtener tortugas de colores distintos.

+ Divertido, sin embargo, tienes que recordar y escribir demasiadas cosas cada vez que quieras una tortuga de color aleatorio y, además, no resulta fácil de leer. 

    En Python podemos escribir `def` para definir una función que recuperaremos cada vez que queramos crear una tortuga con un color aleatorio. 

    Ya has recuperado funciones anteriormente. `color()` y `randint()` son funciones que ha sido definidas para ti. 

    Apliquemos un código de color aleatorio usando `def`:
  
    ![screenshot](images/modern-colour-function.png)
    
  Asegúrate de sangrar el código dentro de la función. Las funciones normalmente se encuentran en la parte superior del script después de las importaciones. 
  
+ Si ejecutas tu código en estos momentos, no obtendrás una tortuga de color aleatorio. Esto se debe a que has definido la función pero todavía no las has recuperado. 
  
+ Añade una línea para recuperar tu nueva función:
  
    ![screenshot](images/modern-call-colour.png)

    Ten en cuenta que tu nuevo código es mucho más fácil de entender porque la parte más compleja es la función. Es muy sencillo averiguar qué es lo que hace `randomcolour()`. 
