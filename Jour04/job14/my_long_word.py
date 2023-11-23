def my_long_word(taille_min, phrase):
    mots = phrase.split()
    mots_filtres = []

    for mot in mots:
        mot = mot.strip(",.")
        if not mot.isnumeric() and len(mot) > taille_min:
            mots_filtres.append(mot)

    resultat = " ".join(mots_filtres)
    return resultat

taille_min = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

output = my_long_word(taille_min, phrase)
print("Output :", output)
