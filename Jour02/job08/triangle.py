def type_triangle(a, b, c):
    
    if a + b > c and a + c > b and b + c > a:
       
        if a == b == c:
            return "Equilatéral"  
        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                return "Rectangle et Isocèle"  
            else:
                return "Isocèle"  
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Rectangle"  
        else:
            return "Quelconque"  
    else:
        return "Impossible de former un triangle"

a = float(input("Entrez la longueur du côté a : "))
b = float(input("Entrez la longueur du côté b : "))
c = float(input("Entrez la longueur du côté c : "))

resultat = type_triangle(a, b, c)

print(f"Le triangle est {resultat}.")
