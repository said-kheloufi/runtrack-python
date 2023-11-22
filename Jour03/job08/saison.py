def affiche_aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        print("Orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("Carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("Artichaut, aubergine, navet")

affiche_aliments("fruits", "hiver")
affiche_aliments("fruits", "ete")
affiche_aliments("legume", "hiver")
affiche_aliments("legume", "ete")
affiche_aliments("poisson", "printemps")        