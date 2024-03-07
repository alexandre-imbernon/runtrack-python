#Créer une fonction qui vérifie que le nombre est pair ou impair. Pensez à
#vérifier si le nombre est bien un chiffre entier et positif.
#Appeler cette fonction plusieurs fois avec des valeurs différentes.

def pair_impair(n):
    if (n % 2) == 0 and n > 0 and int:
        return "pair et positif"
    elif (n % 2) == 0 and n < 0 and int:
        return "pair et négatif" 
    elif (n % 2) != 0 and n > 0 and int:
        return "impair et positif"
    elif (n % 2) != 0 and n < 0 and int:
        return "impair et négatif"
n = int(input("Entrez un nombre: "))
print(pair_impair(n))
