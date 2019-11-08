## Losowe miejsce

Stwórzmy kolejną funkcję, aby przenieść żółwia do losowego miejsca na ekranie. Środek ekranu wynosi (0,0), więc umieszczamy żółwie w kwadratowym obszarze wokół środka.

+ Dodaj funkcję `losowemiejsce()`:
    
    ![zrzut ekranu](images/modern-place-function.png)

+ Wypróbuj nową funkcję, wywołując ją, a następnie wywołując `stamp()`, możesz wywołać ją więcej niż jeden raz:
    
    ![zrzut ekranu](images/modern-call-place.png)

+ Ooops, żółw rysuje, gdy się porusza. Podnieśmy pióro na początku i opuśćmy na końcu, aby żółw nie rysował podczas ruchu:
    
    ![zrzut ekranu](images/modern-place-pen.png)
    
    Czy zauważyłeś, że wystarczy "naprawić" kod w jednym miejscu? To kolejna dobra rzecz w funkcjach.

+ Teraz przetestuj swój kod kilka razy.