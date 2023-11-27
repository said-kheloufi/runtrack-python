def my_sort(lst):
    n = len(lst)
    coups = 0  # Initialisation du compteur de coups
    trie = False  # Variable pour indiquer si la liste est triée

    while not trie:
        trie = True  # On suppose que la liste est triée

        for i in range(n - 1):
            # Comparaison des éléments adjacents
            if lst[i] > lst[i + 1]:
                # Échange des éléments
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                trie = False  # La liste n'est pas encore triée
                coups += 1  # Incrémente le compteur de coups

    return lst, coups

# Exemple d'utilisation
liste_non_triee = [64, 34, 25, 12, 22, 11, 90]
liste_triee, nombre_coups = my_sort(liste_non_triee)

# Affichage des résultats
print("Liste triée     :", liste_triee)
print("Nombre de coups :", nombre_coups)
