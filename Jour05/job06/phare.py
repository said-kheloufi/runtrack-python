def distance_toilettes_par_semaine(nombre_marches, hauteur_marche):
    nombre_jours_semaine = 7
    nombre_allers_retours_par_jour = 2
    
    distance_parcourue_par_aller_retour = (nombre_marches * hauteur_marche) / 100  # Convertit en mètres
    
    distance_parcourue_par_jour = distance_parcourue_par_aller_retour * nombre_allers_retours_par_jour
    
    distance_parcourue_par_semaine = distance_parcourue_par_jour * nombre_jours_semaine
    
    return distance_parcourue_par_semaine

nombre_marches = int(input("Entrez le nombre de marches du phare : "))
hauteur_marche = int(input("Entrez la hauteur de chaque marche en cm : "))

distance_totale = distance_toilettes_par_semaine(nombre_marches, hauteur_marche)

print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")
