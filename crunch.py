import os

#creer un nouveau fichier texte
with open("generate.txt", "w") as fichier:
    for x in range(1, 10000):
        #ecrire le nombre dans le fichier
        fichier.write("\n{:04d}".format(x))

#lire le fichier texte et afficher son contenu
with open("generate.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
