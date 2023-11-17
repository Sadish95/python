import tkinter as tk
from tkinter import messagebox
import sqlite3

class GestionLivresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Livres")

        # Connexion à la base de données SQLite
        self.conn = sqlite3.connect('bibliotheque.db')
        self.cursor = self.conn.cursor()

        # Création de la table Livres si elle n'existe pas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Livres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titre TEXT,
                auteur TEXT,
                genre TEXT,
                isbn TEXT
            )
        ''')
        self.conn.commit()

        # Interface utilisateur
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        tk.Label(self.frame, text="Titre:").grid(row=0, column=0, sticky='e')
        tk.Label(self.frame, text="Auteur:").grid(row=1, column=0, sticky='e')
        tk.Label(self.frame, text="Genre:").grid(row=2, column=0, sticky='e')
        tk.Label(self.frame, text="ISBN:").grid(row=3, column=0, sticky='e')

        self.titre_entry = tk.Entry(self.frame)
        self.auteur_entry = tk.Entry(self.frame)
        self.genre_entry = tk.Entry(self.frame)
        self.isbn_entry = tk.Entry(self.frame)

        self.titre_entry.grid(row=0, column=1)
        self.auteur_entry.grid(row=1, column=1)
        self.genre_entry.grid(row=2, column=1)
        self.isbn_entry.grid(row=3, column=1)

        # Boutons
        tk.Button(self.frame, text="Ajouter Livre", command=self.ajouter_livre).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.frame, text="Rechercher Livre", command=self.rechercher_livre).grid(row=5, column=0, columnspan=2, pady=10)

    def ajouter_livre(self):
        titre = self.titre_entry.get()
        auteur = self.auteur_entry.get()
        genre = self.genre_entry.get()
        isbn = self.isbn_entry.get()

        if titre and auteur and genre and isbn:
            # Ajouter le livre à la base de données
            self.cursor.execute