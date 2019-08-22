## Losowe kolory

+ Otwórz ten szablon: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ Możesz ustawić kolor żółwia mówiąc, ile czerwonego, zielonego i niebieskiego chcesz od 0 do 255.
    
    Dodaj następujący kod, aby uzyskać fioletowego żółwia:
    
    ![zrzut ekranu](images/modern-purple.png)
    
    Fioletowy powstaje przez zmieszanie razem czerwonego i niebieskiego.

\--- collapse \---

* * *

## tytuł: „Błąd - niewłaściwa sekwencja kolorów: (150, 0, 150)”

Czy pojawia się błąd `niewłaściwa sekwencja kolorów: (150, 0, 150)` podczas uruchamiania kodu.

Jest tak, ponieważ bibelot używa innego trybu kolorów niż inne edytory Python. Można to naprawić, zmieniając kolor `` na `255`.

```python
z importu żółwia *

colormode (255)

kształt („żółw”)
kolory (150,0150)
```

\--- /collapse \---

+ Wypróbuj różne liczby, aby uzyskać różne kolory.
    
    Pamiętaj, że każda liczba może wynosić od 0 do 255.

+ Co powiesz na wybór losowego koloru?
    
    Zaktualizuj kod, aby wybrać losową liczbę od 0 do 255 dla wartości czerwonej, zielonej i niebieskiej:
    
    ![zrzut ekranu](images/modern-random-colour.png)

+ Kliknij kilka razy „Uruchom”, aby uzyskać żółwie w różnych kolorach.

+ To zabawne, ale dużo trzeba pamiętać i pisać za każdym razem, gdy chcesz ustawić żółwia na losowy kolor i nie jest to łatwe do odczytania.
    
    W Pythonie możemy napisać `def` aby zdefiniować funkcję, którą możemy wywołać za każdym razem, gdy musimy ustawić żółwia na losowy kolor.
    
    Wywołujesz już funkcje, `color ()` i `randint ()` to funkcje, które zostały zdefiniowane dla Ciebie.
    
    Umieśćmy losowy kod koloru w funkcji za pomocą def:
    
    ![zrzut ekranu](images/modern-colour-function.png)
    
    Upewnij się, że wpisałeś kod wewnątrz funkcji. Funkcje są zwykle umieszczane u góry skryptu po imporcie.

+ Jeśli teraz „uruchomisz” swój kod, nie otrzymasz żółwia o losowych kolorach. To dlatego, że zdefiniowałeś swoją funkcję, ale jeszcze jej nie wywołałeś.

+ Dodaj linię, aby wywołać nową funkcję:
    
    ![zrzut ekranu](images/modern-call-colour.png)
    
    Zauważ, że twój nowy kod jest znacznie łatwiejszy do zrozumienia, ponieważ część złożona jest w funkcji. Łatwo jest ustalić, co robi `losowych kolorów ()`.