# Importer les bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup
import sys
import os
 

# 57
'''
1 : dl la page
2 : cherche dedans numéro ligne &> txt
3 : nettoie fichier txt &> new.txt
4 : découpe la page de [a ; a+57] &> txt_1
5 : nettoie fichier txt_1 &> new.txt_1
'''
class monde:

    def bash_start():
        os.system("./ligne.sh")
        
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

    def clean(a):
                # ouverture du fichier et lecture des lignes
        with open(a, "r") as fichier:
            lines = fichier.readlines()

        # ecriture dans un nouveau fichier
        with open("fichier_nouveau.txt", "w") as fichier_nouveau:
            # parcours chaque ligne du fichier
            for line in lines:
                # parcours chaque mot de la ligne
                for word in line.split():
                    # test si le mot est un int
                    if word.isdigit():
                        # ecriture dans le nouveau fichier
                        fichier_nouveau.write(word + " ")

        # fermeture du fichier
        fichier.close()

    def decoupe():
        #on commence par importer le module sys 

        # on définit les variables pour les lignes de départ et d'arrivée 
        start_line = int(a)
        end_line = int(a+57)

        # on ouvre le fichier et le ligne par ligne 
        with open("source_html.txt", "r") as f:
            lignes = f.readlines()

        # on découpe le fichier entre les lignes de départ et d'arrivée 
        decoupe_fichier = lignes[start_line:end_line]

        # on écrit le nouveau fichier 
        with open("limited.txt", "w", encoding="utf-8") as f:
            for ligne in decoupe_fichier:
                f.write(ligne)


monde.get()
monde.bash_start()