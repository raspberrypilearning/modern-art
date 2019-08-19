## Nasumične boje

+ Otvori ovaj trinket: <a href="https://trinket.io/python/accb90ca4c" target="_blank">jumpto.cc/modern-go</a>.

+ Možeš podesiti boju kornjače tako da odabereš koliko želiš crvene, zelene i plave boje od 0 do 255.
    
    Dodaj sljedeći kôd kako bi tvoja kornjača bila ljubičasta:
    
    ![screenshot](images/modern-purple.png)
    
    Ljubičasta se dobije miješanjem crvene i plave boje.

--- collapse ---
---
title: "Pogreška - loš slijed boja: (150, 0, 150)"
---

Dobivaš li grešku `loš slijed boja(150, 0, 150)` kad pokreneš kreneš svoj program?

To je zato što trinket koristi drugi način rada u bojama za razliku od drugih Python uređivaća. Grešku možeš popraviti postavljanjem `modula boje` na `255`.

```python
from turtle import *

colormode(255)

shape("turtle")
color(150,0,150)
```

--- /collapse ---

+ Pokušaj s nekim drugim brojevima kako bi dobio različite boje.
    
    Zapamti da svaki broj može imati vrijednost od 0 do 255.

+ Kako bi bilo da nasumično odaberemo boju?
    
    Izmijeni svoj kôd tako da za vrijednosti crvene, zelene i plave boje odabere nasumični broj između 0 i 255:
    
    ![screenshot](images/modern-random-colour.png)

+ Klikni na ‘Run’ nekoliko puta da dobiješ kornjače različitih boja.

+ Zabavno je, ali i teško za zapamtiti i unositi svaki put kad želiš da se boja kornjače nasumično odredi. Također je i teško za čitati.
    
    U Pythonu možemo upisati `def` i definirati funkciju koju možemo pozvati svaki put kad želimo nasumično odabrati boju kornjače.
    
    Već smo pozivali funkcije, poput `color()` i `randint()` koje su bile unaprijed definirane.
    
    Iskoristimo def kako bi u funkciju stavili dio kôda koji nasumično određuje boju:
    
    ![screenshot](images/modern-colour-function.png)
    
    Ne zaboravi uvući kôd unutar funkcije. Funkcije se obično pišu na početku programa, nakon naredbi import.

+ Ako sada klikneš na ‘Run’, nećeš dobiti nasumično obojenu kornjaču. To je zato što si definirao svoju funkciju, ali ju nisi pozvao.

+ Dodaj sljedeću liniju kôda za pozivanje svoje nove funkcije:
    
    ![screenshot](images/modern-call-colour.png)
    
    Primijeti da je tvoj novi kôd puno lakši za razumijeti jer je komplicirani dio unutar funkcije. Lako je zaključiti što funkcija `nasumicnaBoja()` radi.