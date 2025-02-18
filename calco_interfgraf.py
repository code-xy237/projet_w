import tkinter as tk

# Fonction pour gérer les clics sur les boutons
def on_click(value):
    if value == '=':
        try:
            result = str(eval(display_var.get()))
            display_var.set(display_var.get() + " = " + result)

        except:
            display_var.set("Erreur de Syntaxe")
    elif value == 'C':
        display_var.set("")
    else:
        current_text = display_var.get()

        # Ajoute le chiffre ou l'operateur au texte afficher
        display_var.set(current_text + value)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Codex Calculator")
root.configure(background='cyan')

# Variable de contrôle pour afficher le texte
display_var = tk.StringVar()
display_var.set("")

# Création du champ d'affichage
display = tk.Entry(root, textvariable=display_var, justify='left', background='cyan', font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4, sticky='ew')

# Liste des boutons de la calculatrice
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Placement des boutons
row = 1
col = 0

for button_text in buttons:
    # Fonction anonyme pour gérer les clics sur les boutons
    command = lambda x=button_text: on_click(x)

    button = tk.Button(root, text=button_text, command=command, background='red', font=("Arial", 20))
    button.grid(row=row, column=col, sticky='nsew')

    col += 1
    if col > 3:
        col = 0
        row += 1

# Redimension des boutons pour qu'ils remplissent l'espace
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()

