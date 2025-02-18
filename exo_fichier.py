#nous creons un programme, un fichier visant a stocker des données dans un fichier precis que nous avons au prealable créer nommer ( create_fichier )
#le fichier qui est créer doit etre sous l'extension .txt
#nous creons un fichier qui stockera plusieur donnée, puis nous y ajouterons une nouvelle donnée dans ce fichier enregistrer

with open ('create_fichier.txt', 'w') as fichier:
    fichier.write("Ceci est la premiere ligne \n")
    fichier.write("Voici la deuxieme ligne \n")
    fichier.write("Et une troisieme ligne \n")

with open ('create_fichier.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)
    
#ici, nous creons une nouvelle ligne ou nouvelle donnée dans notre fichier ( create_fichier.txt)
    #l'on utilise la balise  'a' visant a ajouter de nouvelle donnée dans un fichier
with open ('create_fichier.txt', 'a') as fichier:
    fichier.write("Cette ligne a été ajouté !!!")

with open ('create_fichier.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)

