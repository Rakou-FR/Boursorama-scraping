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

    def find():
        # On commence par ouvrir le fichier
        fichier = open("source_html.txt","r", encoding="UTF-8")

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
        if int(len(liste)) <= 36:
            for i in range(0, len(liste), 3):
                output_list.append(str(liste[i]) + str(liste[i+1]) + str(liste[i+2]))

        if len(liste) >= 39: 
            for i in range(0, len(liste), 3):
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


class world:
    def get():
        # Définir l'URL du site web

        try:
            url = "https://www.boursorama.com/cours/1rPCS/"
            
            # Récupérer le code source HTML
            r = requests.get(url)
            
            # Créer un objet BeautifulSoup
            soup = BeautifulSoup(r.content, "html.parser")
            
            # Obtenir le code source HTML
            html = soup.prettify()
            
            # Sauvegarder le code source HTML dans un fichier
            with open("source_html.txt", "w", encoding="utf-8") as f:
                f.write(html)
            return url
        except:
            return "Please restart the programme"
                

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
                    if lettre.isdigit() or lettre == "." or lettre == "%" or lettre == "E" or lettre == "U" or lettre == "R":
                        # On ajoute l'integer à la liste
                        liste.append(lettre)

        # del liste[len(liste)-5:len(liste)]
        return liste

    def name_entreprise(url):
        name = ""
        

    def former():
        liste = []
        # ouverture 6
        liste_1 = world.clean(world.find("ouverture"),6)
        liste.append("")
        for item in liste_1:
            liste[len(liste)-1] += str(item)
        
        # cloture 6
        liste_2 = world.clean(world.find("clôture veille"),6)
        liste.append("")
        for item in liste_2:
            liste[len(liste)-1] += str(item)

        # + haut 6
        liste_3 = world.clean(world.find("+ haut"),6)
        liste.append("")
        for item in liste_3:
            liste[len(liste)-1] += str(item)

        # + bas 6
        liste_4 = world.clean(world.find("+ bas"),6)
        liste.append("")
        for item in liste_4:
            liste[len(liste)-1] += str(item)

        # volume 6
        liste_5 = world.clean(world.find("capital échangé")-10,3)
        liste.append("")
        for item in liste_5:
            liste[len(liste)-1] += str(item)
        
        # capital 6
        liste_6 = world.clean(world.find("capital échangé"),6)
        liste.append("")
        for item in liste_6:
            liste[len(liste)-1] += str(item)

        # valorisation 6
        liste_7 = world.clean(world.find("valorisation"),6)
        liste.append("")
        for i in range(0,len(liste_7)):
            liste[len(liste)-1] += str(liste_7[i])

        # LIMITE À LA HAUSSE
        liste_8_1 = world.clean(world.find("limite à la baisse")+47,7)
        liste.append("")
        for i in range(0,len(liste_8_1)):
            liste[len(liste)-1] += str(liste_8_1[i])

        # LIMITE À LA BAISSE
        liste_8 = world.clean(world.find("limite à la baisse")+15,7)
        liste.append("")
        for i in range(0,len(liste_8)):
            liste[len(liste)-1] += str(liste_8[i])

        # rendemet 6
        liste_9 = world.clean(world.find("rendement estimé"),6)
        liste.append("")
        for i in range(0,len(liste_9)):
            liste[len(liste)-1] += str(liste_9[i])

        # PER estimé 27
        liste_10 = world.clean(world.find("PER estimé")+10,17)
        liste.append("")
        for i in range(0,len(liste_10)):
            liste[len(liste)-1] += str(liste_10[i])

        # dividende et date dividente 16
        liste_11 = world.clean(world.find("dernier dividende"),6)
        liste.append("")
        for i in range(0,len(liste_11)):
            liste[len(liste)-1] += str(liste_11[i])

        # Dividende net par action
        liste_12 = world.clean(world.find("Dividende net par action"),19)
        liste.append("")
        liste.append("")
        liste.append("")
        temp_1 = ""
        for x in liste_12:
            temp_1 += x
        temp_1 = temp_1.split("R")
        liste[len(liste)-3] = temp_1[0] + "R"
        liste[len(liste)-2] = temp_1[1] + "R"
        liste[len(liste)-1] = temp_1[2] + "R"

        # Rendement
        liste_13 = world.clean(world.find("Dividende net par action")+23,10)
        liste.append("")
        liste.append("")
        liste.append("")
        temp_1 = ""
        for x in liste_13:
            temp_1 += x
        temp_1 = temp_1.split("%")
        liste[len(liste)-3] = temp_1[0] + "%"
        liste[len(liste)-2] = temp_1[1] + "%"
        liste[len(liste)-1] = temp_1[2] + "%"

        # Bénéfice net par action
        liste_14 = world.clean(world.find("Bénéfice net par action"),19)
        liste.append("")
        liste.append("")
        liste.append("")
        temp_1 = ""
        for x in liste_14:
            temp_1 += x
        temp_1 = temp_1.split("R")
        liste[len(liste)-3] = temp_1[0] + "R"
        liste[len(liste)-2] = temp_1[1] + "R"
        liste[len(liste)-1] = temp_1[2] + "R"

        # PER
        liste_15 = world.clean(world.find("Bénéfice net par action")+23,4)
        liste.append("")
        for i in range(0,len(liste_15)):
            liste[len(liste)-1] += str(liste_15[i])

        liste_16 = world.clean(world.find("Bénéfice net par action")+27,2)
        liste.append("")
        for i in range(0,len(liste_16)):
            liste[len(liste)-1] += str(liste_16[i])

        liste_17 = world.clean(world.find("Bénéfice net par action")+29,2)
        liste.append("")
        for i in range(0,len(liste_17)):
            liste[len(liste)-1] += str(liste_17[i])

        return liste


if __name__ == '__main__':
    world.get()
    print(world.former())