def tri_a_bulles_avec_arrondi(liste):
    n = len(liste)

    for i in range(n):
        for j in range(0, n-i-1):
            arrondi1 = int(liste[j])
            arrondi2 = int(liste[j+1])

            if arrondi1 > arrondi2:
                liste[j], liste[j+1] = liste[j+1], liste[j]

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

tri_a_bulles_avec_arrondi(ma_liste)

print("Liste après arrondi et tri :", ma_liste)
