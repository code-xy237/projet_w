import itertools

mot = input("Entrez un mot : ")

#Générer toutes les permutation du mot
permutations = list(set(["".join(p) for p in itertools.permutations(mot)]))

#Afficher les differentes orthographes
print("Differentes possibilités d'orthographes du mot", mot, "sont :")
for p in permutations:
    print(p)

#Afficher le nombre total de possibilités
print("Nombre total de possibilités :", len(permutations))