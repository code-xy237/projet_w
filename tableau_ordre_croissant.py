#ceci est un code qui declare un tabbleau et classe ces 10 nombres (valeurs) par ordre croissant
mon_tableau = [7, 2, 5, 1, 9, 3, 8, 6, 4, 0]

#tri du tableau par ordre croissant // la methode " sort() " est une commande pour classer des nombres par ordre croissant
mon_tableau.sort()

#apres le triage, on affiche le resultat par odre croissant
print("Apres le triage, on peut en deduire que par ordre croissant on a :", mon_tableau)

#tri du tableau par ordre decroissant // la methode " sort(reverse=true) " est une commande pour classer des nombres par ordre croissant
mon_tableau.sort(reverse=True)

#apres le triage, on affiche le resultat par odre croissant
print("Apres le triage, on peut en deduire que par ordre decroissant on a :", mon_tableau)
