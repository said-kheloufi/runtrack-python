def chiffre_cesar(message, decalage):
    resultat = ""
    
    for lettre in message:
        if lettre.isalpha():
            est_majuscule = lettre.isupper()
            lettre = lettre.lower()
            lettre_decalee = chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))
            if est_majuscule:
                lettre_decalee = lettre_decalee.upper()
            resultat += lettre_decalee
        else:
            resultat += lettre
    
    return resultat

# Saisies utilisateur
message_original = input("Entrez le message à chiffrer/déchiffrer : ")
decalage = 3

# Appel de la fonction
message_chiffre = chiffre_cesar(message_original, decalage)

# Affichage des résultats
print("Message original:", message_original)
print("Message chiffré/déchiffré:", message_chiffre)
