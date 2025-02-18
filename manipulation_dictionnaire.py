informations_personnelles={"nom":"Tella", "prenom":"Pavel", "age":16}

#avant la modification du dictionnaire " informations_personnelles " , on an :
print(informations_personnelles)

informations_personnelles["ville"]= "Douala"
informations_personnelles["age"]=informations_personnelles["age"]+4
informations_personnelles.keys()

#apres la modification du dictionnaire " informations_personnelles " , on an :
print(informations_personnelles)

for key, value in  informations_personnelles.items():
    #affichage de l'integralité du contenue du dictionnaire pas a pas
    print(key, ":", value)
