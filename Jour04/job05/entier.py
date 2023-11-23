def remplacer_par_somme_voisins(liste, index):
    if index > 0 and index < len(liste) - 1:
        somme_voisins = liste[index - 1] + liste[index + 1]
        liste[index] = somme_voisins

L = [1, 2, 3, 4, 5]

print("Deuxième valeur de la liste:", L[1])

remplacer_par_somme_voisins(L, 3)

print("Tableau après la modification:", L)

print("Dernière valeur de la liste:", L[4])