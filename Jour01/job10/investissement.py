montant_investissement = 10000  
taux_rendement_annuel = 5

gain_annuel = (taux_rendement_annuel / 100) * montant_investissement
print(f"Gain annuel initial à un taux de {taux_rendement_annuel}% : {gain_annuel:.2f} euros")

montant_investissement += 5000
taux_rendement_annuel += 2

nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_investissement
print(f"Nouveau gain annuel après augmentation du capital et du taux : {nouveau_gain_annuel:.2f} euros")

retrait = 0.10 * montant_investissement
montant_investissement -= retrait
taux_rendement_annuel -= 1

montant_final = montant_investissement + nouveau_gain_annuel
print(f"Montant final de l'investissement après retrait et diminution du taux : {montant_final:.2f} euros")