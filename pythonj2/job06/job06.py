for chiffres in range(1001):
    if chiffres > 1:
        for nombre in range(2, chiffres):
            if (chiffres % nombre) == 0:
                break
        else:
            print(chiffres)