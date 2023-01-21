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

class evolution:
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

    def find():
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


    def clean():
        # On commence par ouvrir le fichier texte
        fichier = open("source_html.txt", "r", encoding="UTF-8")

        # On initialise des variables nécessaires
        liste = []
        ligne_debut = int(evolution.find())
        ligne_fin = int(evolution.find()+94)

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

        del liste[len(liste)-5:len(liste)]
        return liste

    def former(liste):
        output_list = []
        if len(liste) <= 36:
            for i in range(0, len(liste), 3):
                output_list.append(str(liste[i]) + str(liste[i+1]) + str(liste[i+2]))

        if len(liste) >= 39: 
            for i in range(0, 27, 3):
                output_list.append(str(liste[i]) + str(liste[i+1]) + str(liste[i+2]))
            for i in range(27, len(liste), 4):
                output_list.append(str(liste[i]) + str(liste[i+1]) + str(liste[i+2]) + str(liste[i+3]))

        final = [
            int(output_list[0])/100,int(output_list[1])/100,int(output_list[2])/100,
            int(output_list[3])/100,int(output_list[4])/100,int(output_list[5])/100,
            int(output_list[6])/100,int(output_list[7])/100,int(output_list[8])/100,
            int(output_list[9])/100,int(output_list[10])/100,int(output_list[11])/100
        ]
        return final, "evo"


class cours:
    def find():
        # On commence par ouvrir le fichier
        fichier = open('source_html.txt','r', encoding="UTF-8")

        # On demande à l'utilisateur le mot à rechercher
        mot_a_rechercher = str("ouverture")

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


    def clean(a):
        # On commence par ouvrir le fichier texte
        fichier = open("source_html.txt", "r", encoding="UTF-8")

        # On initialise des variables nécessaires
        liste = []
        ligne_debut = int(cours.find())
        ligne_fin = int(cours.find()+a)

        # On lit le fichier ligne par ligne
        for num_ligne, ligne in enumerate(fichier):
            # On vérifie si la ligne se trouve entre la ligne de début et celle de fin
            if ligne_debut <= num_ligne <= ligne_fin:
                # On parcourt la ligne lettre par lettre
                for lettre in ligne:
                    # On vérifie si la lettre correspond à un integer
                    if lettre.isdigit() or lettre == "." or lettre == "%":
                        # On ajoute l'integer à la liste
                        liste.append(lettre)

        # del liste[len(liste)-5:len(liste)]
        return liste

#96
#92

    def former(liste):
        output_list = []
        
        for i in range(0, 24, 6):
            output_list.append(str(liste[i]) + str(liste[i+1]) + str(liste[i+2])
            + str(liste[i+5]) + str(liste[i+4]))

        for i in range(len(liste), 27, 3):
            output_list.append(str(liste[i]) + str(liste[i+1]) + str(liste[i+2]))

        for i in range(27, len(liste), 4):
            output_list.append(str(liste[i]) + str(liste[i+1]) + str(liste[i+2]) 
            + str(liste[i+3]))

        final = [
            int(output_list[0])/100,int(output_list[1])/100,int(output_list[2])/100,
            int(output_list[3])/100,int(output_list[4])/100,int(output_list[5])/100,
            int(output_list[6])/100,int(output_list[7])/100,int(output_list[8])/100,
            int(output_list[9])/100,int(output_list[10])/100,int(output_list[11])/100
        ]
        return final, "evo"


if __name__ == '__main__':
    evolution.get()
    print(cours.find(),"\n")
    print(cours.clean(181),"\n")
    print(cours.former(cours.clean(181)))