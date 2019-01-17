## Moderne Kunst aus Rechtecken erstellen

Lass uns nun einige moderne Kunstwerke erstellen, indem du viele Rechtecke in verschiedenen Größen und Farben zeichnest.

+ Zuerst fügst du den folgenden Code nach dem Challenge-Code am Ende deines Skripts ein, um den Bildschirm nach deiner Schildkröten-Kunst zu löschen und die Schildkröte in ihre normale Richtung zu weisen:
    
    ![screenshot](images/modern-reset.png)

+ Du kannst deinen Schildkröten-Kunst Code auskommentieren, indem du ein `#` an den Beginn jeder Zeile setzt, damit sie beim Programmlauf übersprungen wird, solange du an der Reckteck-Kunst arbeitest. (Dann kannst du ihn später wieder aktivieren, um deine gesamte Arbeit zu zeigen.)
    
    ![screenshot](images/modern-comment.png)

+ Fügen wir nun eine Funktion hinzu, um ein Rechteck mit zufälliger Größe und zufälliger Farbe an einer zufälligen Stelle zu zeichnen!
    
    Füge eine `zeichnerechteck()` Funktion nach deinen anderen Funktionen hinzu:
    
    ![screenshot](images/modern-rect-function.png)
    
    Schaue in `snippets.py` nach etwas Hilfscode, wenn du etwas Zeit sparen möchtest.

+ Füge den folgenden Code am Ende von `main.py` hinzu, um deine neue Funktion aufzurufen:
    
    ![screenshot](images/modern-call-rect.png)
    
    Führe dein Skript einige Male aus, um die Änderung der Höhe und Breite zu sehen.

+ Das Rechteck hat immer dieselbe Farbe und beginnt an derselben Stelle.
    
    Jetzt musst du die Schildkröte auf eine zufällige Farbe setzen und sie an einen zufälligen Ort verschieben. He, hast du nicht bereits Funktionen dafür erstellt? Prima. Du kannst sie einfach am Anfang der zeichnerechteck-Funktion aufrufen:
    
    ![screenshot](images/modern-random-rect.png)
    
    Tja, das war viel weniger Arbeit und es ist viel einfacher zu lesen.

+ Rufen wir nun `zeichnerechteck()` in einer Schleife auf, um coole moderne Kunst zu kreieren:
    
    ![screenshot](images/modern-rect-art.png)

+ Meine Güte, das war ein bisschen langsam, nicht wahr! Glücklicherweise kannst du die Schildkröte beschleunigen.
    
    Suche die Zeile, in der du die Form auf "Schildkröte" setzt, und füge den hervorgehobenen Code hinzu:
    
    ![screenshot](images/modern-speed.png)
    
    `speed(0)` ist die schnellste Einstellung. Du kannst Zahlen von 1 (langsam) bis 10 (schnell) verwenden. Experimentiere, bis du die gewünschte Geschwindigkeit gefunden hast.