student_grades={'alice': 18 , 'bob': 19 , 'charlie': 21 , 'davide': 23}

#ici on uilise une boucle classique pour verifier le plus agé avec la methode " max "
#on utilise " key " pour fouiller les noms et l'age ( les informations ) de la liste pour ressortir et comparer chaque age
etudiant_ages = max(student_grades)
print("l'etudiant le plus agé est ", etudiant_ages, "avec", student_grades[etudiant_ages], "ans")

  #calcul de l'age moyenne de la salle
moyenne_age = sum(student_grades.values()) / len(student_grades)
print("la moyenne d'age des etudiants de la classe est", moyenne_age, "ans")
