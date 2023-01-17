# Importer les bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup
import sys
 
class monde:
    def get():
        # Définir l'URL du site web
        url = "https://www.boursorama.com/cours/1rPSWP/"
        
        # Récupérer le code source HTML
        r = requests.get(url)
        
        # Créer un objet BeautifulSoup
        soup = BeautifulSoup(r.content, "html.parser")
        
        # Obtenir le code source HTML
        html = soup.prettify()
        
        # Sauvegarder le code source HTML dans un fichier
        with open("source_html.txt", "w", encoding="utf-8") as f:
            f.write(html)


    def decoupe(a,b):
        #on commence par importer le module sys 

        # on définit les variables pour les lignes de départ et d'arrivée 
        start_line = int(a)
        end_line = int(b)

        # on ouvre le fichier et le ligne par ligne 
        with open("sample_file.txt", "r") as f:
            lignes = f.readlines()

        # on découpe le fichier entre les lignes de départ et d'arrivée 
        decoupe_fichier = lignes[start_line:end_line]

        # on écrit le nouveau fichier 
        with open("new_file.txt", "w", encoding="utf-8") as f:
            for ligne in decoupe_fichier:
                f.write(ligne)

monde.get()
monde.decoupe(5579,5600)