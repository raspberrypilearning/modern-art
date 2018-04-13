## Losowe kolory

+ Otwórz tę bibelotkę: <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ Możesz ustawić kolor żółwia mówiąc, ile czerwonego, zielonego i niebieskiego chcesz od 0 do 255.
    
    Dodaj następujący kod, aby uzyskać fioletowego żółwia:
    
    ![zrzut ekranu](images/modern-purple.png)
    
    Fioletowy powstaje przez zmieszanie razem czerwonego i niebieskiego.

+ Spróbuj różnych liczb, aby uzyskać różne kolory.
    
    Pamiętaj, że każda liczba może wynosić od 0 do 255.

+ A może wybierzesz losowy kolor?
    
    Zaktualizuj swój kod, aby wybrać liczbę losową z zakresu od 0 do 255 dla wartości czerwonych, zielonych i niebieskich:
    
    ![zrzut ekranu](images/modern-random-colour.png)

+ Kliknij "Run" kilka razy, aby uzyskać różne kolorowe żółwie.

+ To zabawne, ale trzeba pamiętać i pisać za każdym razem, gdy chcesz ustawić żółwia na losowy kolor i nie jest to łatwe do odczytania.
    
    W Pythonie możemy napisać `def` , aby zdefiniować funkcję, którą możemy wywołać, gdy potrzebujemy ustawić żółwia na losowy kolor.
    
    Już wywoływałeś funkcje, `color ()` i `randint ()` to funkcje, które zostały dla ciebie zdefiniowane.
    
    Wstawmy losowy kod koloru do funkcji za pomocą def:
    
    ![zrzut ekranu](images/modern-colour-function.png)
    
    Upewnij się, że wciskasz kod wewnątrz funkcji. Funkcje są zwykle umieszczane u góry skryptu po imporcie.

+ Jeśli teraz uruchomisz swój kod, nie dostaniesz losowego kolorowego żółwia. To dlatego, że zdefiniowałeś swoją funkcję, ale jeszcze nie nazwałeś jej.

+ Dodaj linię, aby zadzwonić do nowej funkcji:
    
    ![zrzut ekranu](images/modern-call-colour.png)
    
    Zauważ, że twój nowy kod jest dużo łatwiejszy do zrozumienia, ponieważ część złożona jest w funkcji. Łatwo ustalić, co robi `randomcolour ()`.