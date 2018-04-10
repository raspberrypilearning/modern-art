## Ein Rechteck in Moderner Kunst erstellen

Lass uns jetzt Moderne Kunst produzieren, indem wir ganz viele Rechtecke in verschiedenen Größen und Farben zeichnen. 

+ Addiere als erstes den folgenden Code zum unteren Teil deines Scripts, nach dem Aufgaben-Code, um den Bildschirm nach deiner Schildkröten-Kunst zu leeren und um die Schildkröte wieder in die normale Richtung zu weisen:

    ![screenshot](images/modern-reset.png)

+ Du kannst deinen Code für das Schildkrötenbild wegkommentieren, indem du ein `#` Rautenzeichen zu Beginner jeder Zeile setzt, damit es nicht läuft, während du an dem Rechteck-Bild arbeitest. (Du kannst diesen Kommentar später wieder entfernen, um dein Gesamtkunstwerk zu zeigen.)

    ![screenshot](images/modern-comment.png)
 
+ Lass uns jetzt eine Funktion hinzufügen, um ein beliebig großes Rechteck mit einer zufällig ausgesuchten Farbe an einem zufällig ausgesuchten Platz zu zeichnen! 
    
    Füge die `drawrectangle()` (Rechteck zeichnen) Funktion nach deinen anderen Funktionen hinzu:

    ![screenshot](images/modern-rect-function.png)
    
    Schau mal unter `snippets.py`, um einen Helfer-Code zu finden, wenn du dir zusätzliche Zeit beim Eintippen ersparen willst. 
    
+ Füge den folgenden Code zum unteren Teil von `main.py`, um deine neue Funktion aufzurufen:

    ![screenshot](images/modern-call-rect.png)
    
    Lass dein Script ein paar Mal laufen, um zu sehen, wie sich die Höhe und Breite verändert. 
   
+ Das Rechteck hat immer die gleiche Farbe und beginnt am gleichen Ort. 

    Jetzt musst du die Schildkröte in einer zufällig ausgesuchten Farbe einstellen und sie dann zu einem zufällig ausgesuchten Platz bewegen. He! Hattest du nicht hierfür bereits schon Funktionen angefertigt? Super. Du kannst diese einfach vom Beginn der Rechteck Funktion aufrufen: 
    
    ![screenshot](images/modern-random-rect.png)
    
    Wow! Das war wesentlich weniger Arbeit und es ist viel leichter zu lesen. 

    
+ Lass uns jetzt die Funktion `drawrectangle()` (Rechteck zeichnen) in einer Schleife aufrufen, um coole Moderne Kunst zu produzieren:

    ![screenshot](images/modern-rect-art.png)

+ Ach herrje! Das hat jetzt aber eine Weile gedauert, nicht wahr?! Glücklicherweise kannst du die Schildkröte schneller laufen lassen. 

    Finde die Linie, in der die Form auf 'turtle' (Schildkröte) einstellst und füge dann den markierten Code hinzu:
    
    ![screenshot](images/modern-speed.png)
    
    `speed(0)` (Geschwindigkeit 0) ist der Schnellste oder du kannst die Zahlen von 1 (langsam) bis 10 (schnell) benutzen. Experimente hiermit ein wenig, bis du deine gewünschte Geschwindigkeit gefunden hast. 
