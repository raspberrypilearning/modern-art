## Créer de l'art moderne rectangulier

Maintenant créons un peu d'art moderne en dessinant plein de rectangles de différentes taille et de couleur.

+ D'abord ajoute le code suivant en bas de ton script, après le code du défi, afin de réinitialiser l'écran après ton art tortuesque et puis pointer la tortue dans sa direction habituelle :

    ![capture d'écran](images/modern-reset.png)

+ Tu peux transformer en commentaire ton art tortuesque en placant un symbole `#` au début de chaque ligne pour que ça ne s'exécute pas pendant que tu travailles sur l'art rectangulier. (Ensuite plus tard tu vas pouvoir enlever le commentaire pour montre tout votre travail.)

    ![capture d'écran](images/modern-comment.png)

+ Maintenant ajoutons une fonction pour écrire un rectangle de taille et de couleur aléatoire à un endroit aléatoire !

    Ajoute une fonction `drawrectangle()` à la suite des autres fonctions :

    ![capture d'écran](images/modern-rect-function.png)

    Regarde dans `snippets.py` pour un peu de code pour t'aider si tu veux passer moins de temps à taper au clavier.

+ Ajoute le code suivant en bas de `main.py` pour appeler ta nouvelle fonction :

    ![capture d'écran](images/modern-call-rect.png)

    Exécute ton script à quelques reprises pour voir l'hauteur et la largeur changer.

+ Le rectangle est toujours la même couleur et commence au même point.

    Maintenant tu auras besoin de paramétrer la tortue avec une couleur aléatoire, puis la bouger à un endoit aléatoire. À ce propos, tu avais déjà crée des fonctions pour faire ça, n'est-ce pas ? Excellent. Tu as juste à les appeler à partir du début de la fonction drawrectangle :

    ![capture d'écran](images/modern-random-rect.png)

    Wow c'était beaucoup moins de travail, et c'était plus facile à lire.


+ Maintenant appelons `drawrectangle()` dans une boucle pour créer de l'art moderne sympa :

    ![capture d'écran](images/modern-rect-art.png)

+ Dis-donc, c'était un peu lent, n'est-ce pas ? Heureusement nous pouvons faire accélérer la tortue.

    Trouve la ligne où tu as paramétré la forme en 'turtle' et ajoute le code en surbrillance :

    ![capture d'écran](images/modern-speed.png)

    `speed(0)` est le plus rapide ou tu peux utiliser les chiffres de 1 (lent) à 10 (rapide.) Faire des essais jusqu'à ce que tu trouves une vitesse qui te plait.
