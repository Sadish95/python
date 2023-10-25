import tkinter as tk

# Fonction pour mettre à jour l'affichage
def bouton_clic(valeur):
    entree_variable.set(entree_variable.get() + str(valeur))

# Fonction pour effacer l'écran
def effacer():
    entree_variable.set("")

# Fonction pour évaluer l'expression
def evaluer():
    try:
        resultat = str(eval(entree_variable.get()))
        entree_variable.set(resultat)
    except:
        entree_variable.set("Erreur")

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("Calculatrice")

# Créer une variable pour stocker l'entrée
entree_variable = tk.StringVar()

# Créer un widget d'entrée
entree = tk.Entry(fenetre, textvariable=entree_variable)
entree.grid(row=0, column=0, columnspan=4)

# Créer les boutons numériques
nombres = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '+', '-',
    '*', '/'
]

row, col = 1, 0
for nombre in nombres:
    tk.Button(fenetre, text=nombre, command=lambda n=nombre: bouton_clic(n)).grid(row=row, column=col)
    col += 1
    if col > 2:
        col = 0
        row += 1

# Boutons spéciaux
tk.Button(fenetre, text='C', command=effacer).grid(row=5, column=0)
tk.Button(fenetre, text='=', command=evaluer).grid(row=5, column=1, columnspan=3)

# Démarrer la boucle principale
fenetre.mainloop()