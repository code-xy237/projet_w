entier = int(input("Entrez un entier : "))

centaine = (entier // 100) % 10 * 100
dizaine = (entier //10) % 10 * 10
unite = entier % 10
print("Apres décomposition , on a pour centaine", centaine)
print("Apres décomposition , on a pour dizaine", dizaine)
print("Apres décomposition , on a pour unité", unite)