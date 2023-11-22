def affiche_positif_negatif(nombre):
    if nombre > 0:
        print("positif")
    elif nombre < 0:
        print("negatif")
    else:
        print("nul")

affiche_positif_negatif(5)
affiche_positif_negatif(-3)
affiche_positif_negatif(0)