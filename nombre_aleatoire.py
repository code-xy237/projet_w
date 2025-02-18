while True:

    nombre = float(input("Entrez un nombre pour deviner le nombre aleatoire gagnant: "))
    import random
    nombre_aleatoire = random . randint(1 , 100)
    if nombre != nombre_aleatoire:
        print("HAHA ☻ ☻ ☻... dommage, vous y etiez presque, c'etait", nombre_aleatoire)
    else:
        print("GREAT ☻ ☻ ☻ !!! Bien jouer , vous avez deviner le nombre gagnant !!! qui est", nombre_aleatoire)

    continuer=input("Voulez vous recommencer le jeu de devinet ... ( Oui / Non ) : ")
    if continuer.lower() != "oui":
        break