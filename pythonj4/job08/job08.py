def somme():
    L = [8,24,27,48,2,16,9,7,84,91]    
    sommes = 0
    for i in L:
      if i % 2 == 0:
        sommes = sommes + i
    return sommes
print(somme())