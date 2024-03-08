def multiple():
    L = [8,24,48,2,16]
    multiples = []
    for i in L:
      if i % 3 == 0:
        multiples.append(i)
    return multiples
print(multiple())

#Ne pas oublier de rajouter une nouvelle liste pour stocker les multiples sinon le print ne se fera que pour le tout premier multiple trouvé