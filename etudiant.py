etudiants = {"Jean": "Homme", "Marie": "Femme", "Pierre": "Homme"}

for etudiant, sexe in etudiants.items():
    if sexe == "Homme":
        print("Bonjour Monsieur", etudiant)
    else:
        print("Bonjour Mademoiselle", etudiant)
