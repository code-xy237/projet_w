nombre = int(input("Entrez un nombre : "))
factorielle = 1

if nombre < 0:
    print("Il n'existe pas de factorielle d'un nombre negatif...!!!")
if nombre == 0:
    print("Le factorielle de 0 est 1 ...!!!")
if nombre == 1:
    print("Le factorielle de 1 est 1! , car 1 * 1 = 1")
else:
    for i in range(1, nombre + 1):
        factorielle = factorielle * i
print("Le factorielle de " , nombre, "est", factorielle)
