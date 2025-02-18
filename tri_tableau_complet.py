#ce code invite l'utilisateur a sasir des nombres dans un tableau , puis ca classe ces nombres dans l'ordre croissant puis decroissant
mon_tableau = input("Entrez des nombre suivis des espace : ")

#la methode " split() " permet de recuperer les nombres contenus dans un chaine de caractere // par exemple la chaine de caractere "mon_tableau"
mon_tableau = mon_tableau.split()

mon_tableau.sort()
print("en croissant on a :", mon_tableau)

mon_tableau.sort(reverse=True)
print("en decroissant on a :", mon_tableau)
