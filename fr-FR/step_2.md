## Couleurs aléatoires

+ Ouvre ce trinket : <a href="http://jumpto.cc/modern-go" target="_blank">jumpto.cc/modern-go</a>.

+ Tu peux définir la couleur d'une tortue en disant combien de rouge, vert et bleu tu voudrais entre les valeurs 0 et 255.

    Ajoute le code suivant afin d'afficher une tortue mauve :

    ![capture d'écran](images/modern-purple.png)

    La couleur mauve est générée en mixant les couleurs rouge et bleu.

+ Essaie des valeurs différents pour trouver des couleurs différentes.

    Pense que chaque valeur doit être entre 0 et 255.

+ Comment choisir un chiffre aléatoire ?

    Mets à jour ton code afin de choisir un chiffre aléatoire entre 0 et 255 pour les valeurs de rouge, vert et bleu :

    ![capture d'écran](images/modern-random-colour.png)

+ Clique ‘Run’ plusieurs fois afin de trouver des couleurs différentes de tortue.

+ C'est rigolo, mais comme ça on doit se souvenir de beauoup de choses et chaque fois tu veux paramétrer une tortue dans une couleur aléatoire ce n'est pas trop facile à lire.

    En Python nous pouvons écrire `def` pour définir une fonction que nous pouvons appeler quand nous avons besoin de paramétrer une tortue avec une couleur aléatoire.

    Tu as déjà appelé des fonctions, `color()` et `randint()` sont des fonctions qui ont été définies pour nous.

    Mettons le code pour une couleur aléatoire dans une fonction utilisant def :

    ![capture d'écran](images/modern-colour-function.png)

  Fais attention de bien décaler le code à l'intérieur de la fonction. Les fonctions sont habituellement placées en haut d'un script juste après les importations.

+ Si tu exécutes (‘Run’) ton code maintenant tu n'auras pas de tortue de couleur aléatoire. C'est parce que tu as défini ta fonction, mais tu ne l'as pas appelé encore.

+ Ajoute une ligne pour appeler ta nouvelle fonction :

    ![capture d'écran](images/modern-call-colour.png)

    Tu peux remarquer que ton nouveau code est beaucoup plus facile à comprendre care la partie compliquée se trouve dans la fonction. C'est facile du coup à comprendre à quoi sert `randomcolour()`.
