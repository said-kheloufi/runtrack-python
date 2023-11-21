nom_produit = "Ordinateur portable"
prix_unitaire = 899.99
quantite_en_stock = 20

print("Informations du Produit:")
print(f"Nom du Produit: {nom_produit}")
print(f"Prix Unitaire: ${prix_unitaire:.2f}")  
print(f"Quantité en Stock: {quantite_en_stock} unités")


quantite_acheter = int(input("Combien d'unités souhaitez-vous acheter ? "))

nouvelle_quantite_stock = quantite_en_stock - quantite_acheter

augmentation_prix = 0.10
nouveau_prix_unitaire = prix_unitaire * (1 + augmentation_prix)

print("\nInformations Mises à Jour:")
print(f"Quantité en Stock après achat de {quantite_acheter} unités: {nouvelle_quantite_stock} unités")
print(f"Nouveau Prix Unitaire (avec 10% d'augmentation): ${nouveau_prix_unitaire:.2f}")