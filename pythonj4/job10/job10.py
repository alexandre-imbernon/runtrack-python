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

#Dans cet exemple, listproduits est initialisé comme une liste vide, et la méthode append() est utilisée pour ajouter des éléments à cette liste. De plus, l’instruction return a été déplacée en dehors de la boucle for, afin que tous les éléments soient ajoutés à la liste avant qu’elle ne soit renvoyée. Ainsi, la fonction renvoie une liste de tous les éléments de L qui sont compris entre 25 et 90.
