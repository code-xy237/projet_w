nombre = float(input("Entrez un nombre : "))
if nombre > 1:
        if (nombre % 2) == 0:
            print(nombre, "n'est pas un nombre premier...!!!")
        if (nombre % 2) != 0:
            print(nombre, "est un nombre premier...!!!")
if nombre < 1:
    print("...Erreur inconnue , il n'existe pas de nombre premier inferieur a 1...!!!")
