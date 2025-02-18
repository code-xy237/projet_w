# Exemple basique de chatbot
name_user = input("Salut chez utilisateur X 🙋🏽 , veillez renseigner votre nom pour continuer : \n")
while True:
    user_input = input("\nVous: ")
    # Logique de réponse du chatbot
    if user_input.lower() == 'bonjour' or 'salut' or 'hello' or 'hier' or 'coucou' or 'cc' or 'bjr' or 'slt':
        print("Chatbot: Bonjour utilisateur", name_user, " 🤗 j'espère que vous allez bien , que puis je faire pour vous aujourd'hui😃\n")
    elif user_input.lower() == 'au revoir':
        print("Chatbot: Au revoir!")
    else:
        print("Chatbot: Désolé, je ne comprends pas.")