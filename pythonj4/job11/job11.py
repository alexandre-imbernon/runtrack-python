def valueup():
    L = [7, 11, 42, 39, 2]    
    L = [i + 1 for i in L]
    return L  

print(valueup())

#i + 1 : Cette ligne est placée avant la boucle for, donc i n’est pas défini à ce moment-là. De plus, le résultat de i + 1 n’est pas stocké ou utilisé, donc cette ligne n’a pas d’effet.
#for i in L: : Cette boucle for parcourt chaque élément i dans L, mais elle ne modifie pas les valeurs dans L.
#return L : Cette instruction est à l’intérieur de la boucle for, donc la fonction se termine et renvoie L après la première itération. Pour renvoyer le résultat final après que toutes les modifications ont été faites, return L doit être placé à l’extérieur de la boucle for.
