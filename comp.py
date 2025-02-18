#ceci fait la somme des carees des nombres pairs dans la liste A et affiche cette somme a chaque iteration (pas a pas...)
A = [2,2,4,5,6,7,8,9,10]
S = 0
for i in A: #on declare " i " qui sera notre compteur pour parcourir les donnees de la liste A
    r = i%2 #ici, ca detecte qu'un nombre est potentiellement dans la liste, car " i " parcourt pas a pas chaque elements de la liste A pour le diviser mathematiquement par 2
    if r == 0: #par la, on detecte que si le reste de la division par 2 est a zero (0) , alors ce nombre est mathematiquement et forcement paire
        S = S + (i * i) #la, ca fait le carree de chaque nombre paire 
        print(S)
print("Apres calcul, l'on peut en deduire que la somme des carées des nombres paires de cette liste est :", S)
