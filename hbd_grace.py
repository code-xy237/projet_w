import tkinter as tk

def afficher_etoile():
    canvas.create_polygon(50, 10, 70, 90, 130, 90, 90, 130, 110, 10, fill='white')

def afficher_coeur():
    bgcolor='orange'
    color='red'
    begin_fill=()
    pensize='5'
    left=(50)
    forward=(133)
    circle=(50,200)
    right=(140)
    circle=(50,200)
    forward=(133)
    end_fill=()

fenetre = tk.Tk()
fenetre.title("Programme Python")
fenetre.configure(background='yellow')

canvas = tk.Canvas(fenetre, width=200, height=200)
canvas.pack()

bouton_etoile = tk.Button(fenetre, text="Afficher étoile", command=afficher_etoile)
bouton_etoile.pack()

bouton_coeur = tk.Button(fenetre, text="Afficher cœur", command=afficher_coeur)
bouton_coeur.pack()

message_label = tk.Label(fenetre, text="Joyeux anniversaire", font=("Arial", 20), bg='yellow')
message_label.pack()

fenetre.mainloop()
