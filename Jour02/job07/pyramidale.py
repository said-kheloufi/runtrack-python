def afficher_pyramide(chaine):
    longueur = len(chaine)

    for i in range(1, longueur * 2, 2):
       sous_chaine = chaine[:i]
       print(sous_chaine)

chaine = "abcdefghijklmnopqrstuvwxyz"
afficher_pyramide(chaine)