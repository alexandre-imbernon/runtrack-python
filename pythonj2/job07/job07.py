# Chaîne initiale
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialisation des variables
i = 0
j = 0
pyramide = ""

# Boucle pour construire la pyramide
while i < len(chaine):
    pyramide += chaine[i:i+j+1] + "\n"
    i += j + 1
    j += 1

# Affichage de la pyramide
print(pyramide)