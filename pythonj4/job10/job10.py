def listproduit():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    listproduits = []
    produit = 1
    for i in L:
        if 25 < i < 90:
            listproduits.append(i)
            produit *= i 
    return produit  

print(listproduit())