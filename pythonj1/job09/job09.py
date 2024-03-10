info = "sont bios en provenance de France."
prix = float (2.50)
qté = int (6)

print(f"Nos melons: {info}")
print(f"Le tarif à l'unité est de: {prix}€")
print(f"Nous avons actuellement: {qté} melons en stock")
      
qté_buy = int(input("Combien souhaitez vous en acheter ? "))
if  qté_buy <= qté:
    qté -= qté_buy
    print(f"C'est noté, merci pour votre achat! Il nous reste actuellement {qté} melons en stock.")
else:
    print("Désolé, nous sommes à court de melons.")
prix *= 1.10
print(f"Malheureusement nos melons ne sont pas épargnés par l'inflation, le nouveau tarif à l'unité est de : {prix}€ (+10%)")