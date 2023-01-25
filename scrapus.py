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
    def find(a):
        # On commence par ouvrir le fichier
        fichier = open('source_html.txt','r', encoding="UTF-8")

        # On demande à l'utilisateur le mot à rechercher
        mot_a_rechercher = str(a)

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


    def clean(a,b):
        # On commence par ouvrir le fichier texte
        fichier = open("source_html.txt", "r", encoding="UTF-8")

        # On initialise des variables nécessaires
        liste = []
        ligne_debut = int(a)
        ligne_fin = int(b+a)

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

    def former():
        liste = []
        # ouverture 6
        liste_1 = cours.clean(cours.find("ouverture"),6)
        liste.append("ouverture :")
        for item in liste_1:
            liste[len(liste)-1] += str(item)
        
        # cloture 6
        liste_2 = cours.clean(cours.find("clôture veille"),6)
        liste.append("cloture :")
        for item in liste_2:
            liste[len(liste)-1] += str(item)

        # + haut 6
        liste_3 = cours.clean(cours.find("+ haut"),6)
        liste.append("+ haut : ")
        for item in liste_3:
            liste[len(liste)-1] += str(item)

        # + bas 6
        liste_4 = cours.clean(cours.find("+ bas"),6)
        liste.append("+ bas : ")
        for item in liste_4:
            liste[len(liste)-1] += str(item)

        # volume 6
        liste_5 = cours.clean(cours.find("capital échangé")-10,3)
        liste.append("volume : ")
        for item in liste_5:
            liste[len(liste)-1] += str(item)
        
        # capital 6
        liste_6 = cours.clean(cours.find("capital échangé"),6)
        liste.append("capital : ")
        for item in liste_6:
            liste[len(liste)-1] += str(item)

        # valorisation 6
        liste_7 = cours.clean(cours.find("valorisation"),6)
        liste.append("valorisation : ")
        for i in range(0,len(liste_7)):
            liste[len(liste)-1] += str(liste_7[i])

        # LIMITE À LA HAUSSE
        liste_8_1 = cours.clean(cours.find("limite à la baisse")+47,7)
        liste.append("lim hausse : ")
        for i in range(0,len(liste_8_1)):
            liste[len(liste)-1] += str(liste_8_1[i])

        # LIMITE À LA BAISSE
        liste_8 = cours.clean(cours.find("limite à la baisse")+15,7)
        liste.append("lim baisse : ")
        for i in range(0,len(liste_8)):
            liste[len(liste)-1] += str(liste_8[i])

        # rendemet 6
        liste_9 = cours.clean(cours.find("rendement estimé"),6)
        liste.append("rendement : ")
        for i in range(0,len(liste_9)):
            liste[len(liste)-1] += str(liste_9[i])

        # PER estimé 27
        liste_10 = cours.clean(cours.find("PER estimé")+10,17)
        liste.append("PER : ")
        for i in range(0,len(liste_10)):
            liste[len(liste)-1] += str(liste_10[i])

        # dividende et date dividente 16
        liste_11 = cours.clean(cours.find("dernier dividende"),6)
        liste.append("dividende : ")
        for i in range(0,len(liste_11)):
            liste[len(liste)-1] += str(liste_11[i])

        return liste


if __name__ == '__main__':
    evolution.get()
    print(cours.former())