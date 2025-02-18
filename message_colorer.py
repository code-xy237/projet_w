from colorama import Fore, init, Back, Style

# Initialiser colorama
init(autoreset=True)

# Message à colorer
message = "Voici un message coloré en rouge et en vert !"

# Colorer le message en rouge
message_colore_rouge = f"\n{Fore.RED}{message}\n"

# Colorer le message en vert
message_colore_vert = f"{Fore.GREEN}{message}\n"

# Afficher les messages colorés
print(message_colore_rouge)
print(message_colore_vert)