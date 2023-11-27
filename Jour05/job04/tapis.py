def afficher_tapis_diagonale(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print(" ", end=" ")  
            else:
                print("#", end=" ")  
        print()  

afficher_tapis_diagonale(10)
