## Crea arte moderna rettangolare

Ora creiamo dell'arte moderna disegnando tanti rettangoli di diversa misura e colore.

+ Prima aggiungiamo il seguente codice al fondo del tuo script, dopo il tuo codice sfida, per ripulire lo schermo dopo l'arte della tartaruga e puntiamo la tartaruga nella sua solita direzione:

    ![screenshot](images/modern-reset.png)

+ Puoi commentare l'arte della tua tartaruga posizionando un `#` all'inizio di ogni linea così che non venga eseguito mentre lavori all'arte dei rettangoli. (Puoi sempre eliminare il commento dopo per esibire la tua opera).

    ![screenshot](images/modern-comment.png)

+ Ora aggiungiamo una funzione per disegnare un rettangolo che abbia una misura a caso, un colore a caso e una posizione a caso!

    Aggiungiamo una funzione `drawrectangle()` dopo le tue altre funzioni:

    ![screenshot](images/modern-rect-function.png)

    Se vuoi risparmiare del tempo in digitare, guarda in `snippets.py` per un codice che ti possa aiutare.  

+ Aggiungi il seguente codice al fondo di 'main.py' per chiamare la tua nuova funzione:

    ![screenshot](images/modern-call-rect.png)

    Esegui diverse volte il tuo script per vedere il cambiamento di altezza e larghezza.

+ Il rettangolo è sempre dello stesso colore e inizia alla stessa posizione.

    Ora dovrai assegnare alla tartaruga un colore a caso e poi muoverla verso un luogo a caso. Ma, aspetta, non hai già creato delle funzioni per quello? Fantastico. Semplicemente chiamale dall'inizio della funzione 'drawrectangle':

    ![screenshot](images/modern-random-rect.png)

    Incredibile, senza fatica e molto più facile da leggere.


+ Ora chiamiamo 'drawrectangle()' in loop per creare bella arte moderna:

    ![screenshot](images/modern-rect-art.png)

+ Accidenti, un poco lento, vero? Per fortuna, puoi accelerare la tartaruga.

    Trova la linea dove hai regolato la forma della 'tartaruga' e aggiungi il codice evidenziato:

    ![screenshot](images/modern-speed.png)

    'speed(0)' è la più veloce o puoi usare numeri che vanno da 1 (lento) a 10 (veloce). Sperimenta fino ad ottenere la velocità che preferisci.
