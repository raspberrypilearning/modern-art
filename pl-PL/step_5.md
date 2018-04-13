## Twórz prostokąt sztuki nowoczesnej

Teraz stwórzmy nowoczesną sztukę, rysując wiele prostokątów o różnych rozmiarach i kolorach.

+ Najpierw dodaj poniższy kod na końcu skryptu, po kodzie wyzwania, aby wyczyścić ekran po swojej żółwiowej sztuce i skieruj żółwia w zwykłym kierunku:
    
    ![zrzut ekranu](images/modern-reset.png)

+ Możesz skomentować swój kod sztuki żółwia, umieszczając `#` na początku każdego wiersza, aby nie działał podczas pracy nad prostokątem. (Następnie możesz odkomentować to później, aby pochwalić się całą swoją pracą.)
    
    ![zrzut ekranu](images/modern-comment.png)

+ Teraz dodajmy funkcję losowego losowego prostokąta w przypadkowym miejscu!
    
    Dodaj funkcję `drawrectangle ()` po innych funkcjach:
    
    ![zrzut ekranu](images/modern-rect-function.png)
    
    Zajrzyj do `snippets.py` , aby uzyskać kod pomocnika, jeśli chcesz zaoszczędzić trochę czasu na pisanie.

+ Dodaj następujący kod u dołu `main.py` , aby wywołać nową funkcję:
    
    ![zrzut ekranu](images/modern-call-rect.png)
    
    Uruchom skrypt kilka razy, aby zobaczyć zmianę wysokości i szerokości.

+ Prostokąt ma zawsze ten sam kolor i zaczyna się w tym samym miejscu.
    
    Teraz musisz ustawić żółwia na losowy kolor, a następnie przenieść go do losowego miejsca. Hej, czy nie stworzyłeś już funkcji, by to zrobić? Niesamowite. Możesz po prostu wywołać je od początku funkcji drawrectangle:
    
    ![zrzut ekranu](images/modern-random-rect.png)
    
    Wow to było o wiele mniej pracy i dużo łatwiej było ją przeczytać.

+ Teraz dzwońmy `drawrectangle ()` w pętli, aby stworzyć fajną sztukę współczesną:
    
    ![zrzut ekranu](images/modern-rect-art.png)

+ Gosh, który był nieco powolny, prawda! Na szczęście możesz przyspieszyć żółwia.
    
    Znajdź linię, w której ustawisz kształt na "żółwia" i dodaj wyróżniony kod:
    
    ![zrzut ekranu](images/modern-speed.png)
    
    `szybkość (0)` to najszybsza lub możesz użyć liczb od 1 (wolny) do 10 (szybki.) Eksperyment, dopóki nie znajdziesz prędkości, którą lubisz.