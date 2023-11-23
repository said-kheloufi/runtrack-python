L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

elements_dans_intervalle = [x for x in L if 25 <= x <= 90]

produit_elements_intervalle = 1
for nombre in elements_dans_intervalle:
    produit_elements_intervalle *= nombre

print("Les éléments dans l'intervalle [25, 90] :", elements_dans_intervalle)
print("Le produit des éléments dans l'intervalle :", produit_elements_intervalle)
