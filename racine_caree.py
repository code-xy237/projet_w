while True:
    import math

    racine_caree = float(input("Entrez votre nombre pour calculer automatiquement sa racine caree : "))
    racine = math.sqrt(racine_caree)
    print(racine)
    continuer = input("Voulez vous continuez ...(oui / non) : ")
    if continuer.lower() != "oui":
        break
