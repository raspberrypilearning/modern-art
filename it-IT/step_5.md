## Crea arte moderna rettangolare

Ora creiamo un po' di arte moderna disegnando tanti rettangoli di diverse dimensioni e colori.

+ Prima aggiungi questo codice alla fine del tuo script, dopo il codice dell'ultima sfida, per cancellare lo schermo dopo l'ultima opera artistica con la tartaruga e far puntare la tartaruga nella direzione originale:
    
    ![screenshot](images/modern-reset.png)

+ Puoi commentare parte del tuo codice posizionando un `#` all'inizio di ogni riga in modo che non venga eseguito mentre realizzi le tue opere d'arte rettangolari. (In seguito potrai rimuoverli per mostrare il tuo lavoro al completo.)
    
    ![screenshot](images/modern-comment.png)

+ Ora aggiungiamo una funzione per disegnare un rettangolo di dimensioni, colore e posizione casuali!
    
    Aggiungi una funzione `disegnarettangolo()` dopo le altre funzioni:
    
    ![screenshot](images/modern-rect-function.png)
    
    Cerca in `snippets.py` per qualche codice d'aiuto se vuoi risparmiare un po' di tempo.

+ Aggiungi questo codice nella parte inferiore di `main.py` per chiamare la tua nuova funzione:
    
    ![screenshot](images/modern-call-rect.png)
    
    Esegui il tuo script alcune volte per vedere come cambiano altezza e larghezza.

+ Il rettangolo è sempre dello stesso colore e inizia nella stessa posizione.
    
    Ora dovrai impostare la tartaruga su un colore casuale e poi spostarla in una posizione casuale. Ehi, ma non hai già creato delle funzioni per farlo? Meraviglioso. Puoi chiamarle semplicemente all'inizio della funzione disegnarettangolo:
    
    ![screenshot](images/modern-random-rect.png)
    
    Wow, è bastato veramente poco ed il codice ed è molto più facile da leggere.

+ Ora chiamiamo `drawrectangle()` dentro un ciclo per creare dell'arte moderna:
    
    ![screenshot](images/modern-rect-art.png)

+ Accidenti! Era un po' lento, no? Fortunatamente puoi far accelerare la tartaruga.
    
    Trova la linea in cui imposti la forma "turtle" e aggiungi il codice evidenziato:
    
    ![screenshot](images/modern-speed.png)
    
    `speed(0)` è il più veloce ma puoi usare numeri compresi tra 1 (lento) e 10 (veloce). Prova fino a trovare la velocità che ti preferisci.