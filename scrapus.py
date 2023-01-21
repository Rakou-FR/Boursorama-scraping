# Importer les bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup
import sys
import os
 
# 94
# 57
'''
1 : dl la page
2 : cherche dedans numéro ligne &> txt
3 : nettoie fichier txt &> new.txt
4 : découpe la page de [a ; a+57] &> txt_1
5 : nettoie fichier txt_1 &> new.txt_1
'''

class world:
    def get():
        # Définir l'URL du site web
        url = input("put the boursorama society link : ")
        
        # Récupérer le code source HTML
        r = requests.get(url)
        
        # Créer un objet BeautifulSoup
        soup = BeautifulSoup(r.content, "html.parser")
        
        # Obtenir le code source HTML
        html = soup.prettify()
        
        # Sauvegarder le code source HTML dans un fichier
        with open("source_html.txt", "w", encoding="utf-8") as f:
            f.write(html)

    def find_evolution():
        # On commence par ouvrir le fichier
        fichier = open('source_html.txt','r', encoding="UTF-8")

        # On demande à l'utilisateur le mot à rechercher
        mot_a_rechercher = str("Dividende net par action")

        # On crée un compteur pour le numéro de ligne
        numero_ligne = 0

        # On parcourt le fichier ligne par ligne
        for ligne in fichier:
            # On incrémente le numéro de ligne
            numero_ligne = numero_ligne + 1
            # On cherche le mot
            if mot_a_rechercher in ligne:
                # On affiche le numéro de ligne
                return numero_ligne

        # On ferme le fichier
        fichier.close()


    def clean_v1():
        # On commence par ouvrir le fichier texte
        fichier = open("source_html.txt", "r", encoding="UTF-8")

        # On initialise des variables nécessaires
        liste = []
        ligne_debut = int(world.find_evolution())
        ligne_fin = int(world.find_evolution()+94)

        # On lit le fichier ligne par ligne
        for num_ligne, ligne in enumerate(fichier):
            # On vérifie si la ligne se trouve entre la ligne de début et celle de fin
            if ligne_debut <= num_ligne <= ligne_fin:
                # On parcourt la ligne lettre par lettre
                for lettre in ligne:
                    # On vérifie si la lettre correspond à un integer
                    if lettre.isdigit():
                        # On ajoute l'integer à la liste
                        liste.append(lettre)

        del liste[39:44]


        output_list = []
        for i in range(0, 27, 3):
            output_list.append(liste[i] + liste[i+1] + liste[i+2])

        for i in range(27, len(liste), 4):
            output_list.append(liste[i] + liste[i+1] + liste[i+2] + liste[i+3])


        final = [
            int(output_list[0])/100,int(output_list[1])/100,int(output_list[2])/100,
            int(output_list[3])/100,int(output_list[4])/100,int(output_list[5])/100,
            int(output_list[6])/100,int(output_list[7])/100,int(output_list[8])/100,
            int(output_list[9])/100,int(output_list[10])/100,int(output_list[11])/100
        ]
        return final

    def limiter(a):
        #on commence par importer le module sys 

        # on définit les variables pour les lignes de départ et d'arrivée 
        start_line = int(world.find_evolution())
        end_line = int(world.find_evolution()+a)

        # on ouvre le fichier et le ligne par ligne 
        with open("source_html.txt", "r", encoding="utf-8") as f:
            lignes = f.readlines()

        # on découpe le fichier entre les lignes de départ et d'arrivée 
        decoupe_fichier = lignes[start_line:end_line]

        # on écrit le nouveau fichier 
        with open("limiter.txt", "w", encoding="utf-8") as f:
            for ligne in decoupe_fichier:
                f.write(ligne)

    def test():
        # début du programme 

        # ouverture du fichier en lecture
        fichier_texte = open("limited.txt", "r", encoding="utf-8")

        # création d'une variable pour stocker le texte sans lettres
        texte_sans_lettres = []

        # lecture du fichier ligne par ligne
        for ligne in fichier_texte:
            # parcourir chaque caractère de la ligne et ne garder que les chiffres
            for caractere in ligne:
                if caractere.isdigit():
                    texte_sans_lettres.append(caractere)

        # fermer le fichier
        fichier_texte.close()

        return texte_sans_lettres

    def former(who,liste):
        del liste[39:44]


        output_list = []
        for i in range(0, 27, 3):
            output_list.append(liste[i] + liste[i+1] + liste[i+2])

        for i in range(27, len(liste), 4):
            output_list.append(liste[i] + liste[i+1] + liste[i+2] + liste[i+3])


        final = [
            int(output_list[0])/100,int(output_list[1])/100,int(output_list[2])/100,
            int(output_list[3])/100,int(output_list[4])/100,int(output_list[5])/100,
            int(output_list[6])/100,int(output_list[7])/100,int(output_list[8])/100,
            int(output_list[9])/100,int(output_list[10])/100,int(output_list[11])/100
        ]
        return final

if __name__ == '__main__':
    world.get()
    print(world.find_evolution())
    print(world.clean_v1())
    world.limiter(94)
    print(world.test())