from itertools import permutations

def generate_spellings(word):
    possible_spellings = set()
    word_length = len(word)

    for perm in permutations(word):
        possible_spellings.add(''.join(perm))

        return possible_spellings
    
def test_spellings(word):
    possible_spellings = generate_spellings(word)
    valid_spellings = set()

    #tester les differentes possibilités
    for spelling in possible_spellings:
        if spelling != word: #Assurer que le mot original n'est pas inclus

            #Ici , on ajoute les regles supplementaires pour determiner si un mot est une orthographe valide

            valid_spellings.add(spelling)

    return valid_spellings, len(valid_spellings)
#Saisie du mot par l'utilisateur
user_word = input("Entrez un mot : ")

#Generer et tester les differents possibilités d'ecriture orthographique
valid_spellings, total_valid_spellings = test_spellings(user_word)

#Afficher les resultats
print("Les orthographes valides pour '{}' sont :".format(user_word))
for valid_spelling in valid_spellings:
    print(valid_spelling)

print("Nombre total de possibilités d'ecriture orthographique : ", total_valid_spellings)