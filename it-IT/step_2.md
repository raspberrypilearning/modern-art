## Colori casuali

+ Apri questo trinket: <a href="https://trinket.io/python/8edd3dc48d" target="_blank">jumpto.cc/modern-go</a>.

+ Puoi impostare il colore di una tartaruga scegliendo la quantità di rosso, verde e blu che desideri da 0 a 255.
    
    Aggiungi il seguente codice per ottenere una tartaruga viola:
    
    ![screenshot](images/modern-purple.png)
    
    Il viola è ottenuto mescolando insieme rosso e blu.

+ Prova valori diversi per ottenere colori diversi.
    
    Ricorda che ogni numero può essere compreso tra 0 e 255.

+ Che ne dici di scegliere un colore casuale?
    
    Aggiorna il codice per scegliere un numero casuale compreso tra 0 e 255 per i valori rosso, verde e blu:
    
    ![screenshot](images/modern-random-colour.png)

+ Fai clic su "Esegui" un paio di volte per ottenere tartarughe di colori diversi.

+ È divertente, ma devi ricordare e scrivere molto codice ogni volta che vuoi impostare una tartaruga su un colore casuale. In più non è molto facile da leggere.
    
    In Python possiamo scrivere `def` per definire una funzione che possiamo chiamare ogni volta che è necessario far comparire una tartaruga di colore diverso.
    
    Hai già chiamato funzioni in precedenza, `color()` e `randint()` sono funzioni che abbiamo definito per te.
    
    Mettiamo il codice del colore casuale in una funzione usando def:
    
    ![screenshot](images/modern-colour-function.png)
    
    Assicurati di indentare il codice all'interno della funzione. Le funzioni vengono generalmente posizionate nella parte superiore dello script dopo le istruzioni di import.

+ Se ora clicchi su "Run" non ottieni una tartaruga colorata casualmente. Questo perché hai definito la tua funzione, ma non l'hai ancora chiamata.

+ Aggiungi una linea per chiamare la tua nuova funzione:
    
    ![screenshot](images/modern-call-colour.png)
    
    Nota che il tuo nuovo codice è molto più facile da capire perché la parte complessa è nella funzione. È facile capire cosa `colorecasuale()` faccia.