mon_tableau = input("Entrez les elments a traiter : ")
mon_tableau = mon_tableau.split()

mon_tableau.sort()
print("par croissant, on a : ", mon_tableau)

somme = sum(mon_tableau)
print("la somme est : ", somme)

moyenne = somme / len(mon_tableau)
print("la moyenne est : ", moyenne)
