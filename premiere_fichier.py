with open('start.txt', 'w') as fichier:
    fichier.write ('Hello world !')

with open('start.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)

with open('campus.txt', 'w') as fichier:
    fichier.write ('Bienvenue dans notre campus ...!\n')

with open('campus.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)

    
