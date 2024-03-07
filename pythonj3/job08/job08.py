def szn(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine, kiwi")
    elif type == "fruits" and saison == "ete":
        print("poire, fraise, cassis")
    elif type == "legumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legumes" and saison == "ete":
        print("artichaut, aubergine, navet")
szn("legumes","hiver")