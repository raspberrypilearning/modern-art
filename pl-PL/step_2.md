## Losowe kolory

+ Otwórz ten szablon: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ Możesz ustawić kolor żółwia mówiąc, ile chcesz czerwonego, zielonego i niebieskiego od 0 do 255.
    
    Dodaj następujący kod, aby uzyskać fioletowego żółwia:
    
    ![zrzut ekranu](images/modern-purple.png)
    
    Fioletowy powstaje przez zmieszanie czerwonego i niebieskiego.

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

+ Wypróbuj różne liczby, aby uzyskać różne kolory.
    
    Pamiętaj, że każda liczba może być od 0 do 255.

+ Co powiesz na wybór losowego koloru?
    
    Popraw kod, aby wybrać losową liczbę od 0 do 255 dla czerwonego, zielonego i niebieskiego:
    
    ![zrzut ekranu](images/modern-random-colour.png)

+ Kliknij kilka razy „Run”, aby uzyskać żółwie w różnych kolorach.

+ To fajne, ale dużo trzeba pamiętać i pisać za każdym razem, gdy chcesz ustawić żółwia na losowy kolor i nie jest to łatwe do odczytania.
    
    W Pythonie możemy napisać `def` aby zdefiniować funkcję, którą możemy wywołać za każdym razem, gdy musimy ustawić żółwia na losowy kolor.
    
    Wywoływałeś już wcześniej funkcje, `color()` i `randint()` to funkcje, które zostały zdefiniowane dla Ciebie.
    
    Umieśćmy losowy kod koloru w funkcji za pomocą def:
    
    ![zrzut ekranu](images/modern-colour-function.png)
    
    Upewnij się, że wpisałeś ten kod wewnątrz funkcji. Funkcje są zwykle umieszczane u góry skryptu po imporcie.

+ Jeśli teraz uruchomisz swój kod wciskając "Run", nie otrzymasz żółwia o losowych kolorach. To dlatego, że zdefiniowałeś swoją funkcję, ale jeszcze jej nie wywołałeś.

+ Dodaj linię, aby wywołać nową funkcję:
    
    ![zrzut ekranu](images/modern-call-colour.png)
    
    Zauważ, że twój nowy kod jest znacznie łatwiejszy do zrozumienia, ponieważ jego skomplikowana część jest w funkcji. Łatwo jest ustalić, co robi `randomcolour()`.