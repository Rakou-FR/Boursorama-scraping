import pandas as pd 
import scrap as sp
import requests


class csv:
    def create(liste,link):
        # list of name, degree, score
        #nom = [liste[len(liste)-1]]
        ouverture = [liste[0]]
        cloture = [liste[1]]
        plus_haut = [liste[2]]
        plus_bas = [liste[3]]
        volume = [liste[4]]
        capital = [liste[5]]
        valorisation = [liste[6]]
        lim_hausse = [liste[7]]
        lim_baisse = [liste[8]]
        rendement = [liste[9]]
        per = [liste[10]]

        dividende_2022 = [liste[12]]
        dividende_2023 = [liste[13]]
        dividende_2024 = [liste[14]]

        rendement_2022 = [liste[15]]
        rendement_2023 = [liste[16]]
        rendement_2024 = [liste[17]]

        benefice_2022 = [liste[18]]
        benefice_2023 = [liste[19]]
        benefice_2024 = [liste[20]]

        per_2022 = [liste[21]]
        per_2023 = [liste[22]]
        per_2024 = [liste[23]]
        
            
        # dictionary of lists  
        dict = { 
            "Ouverture" : ouverture,
            "Cloture" : cloture,
            "+ haut" : plus_haut,
            "+ bas " : plus_bas,
            "Volume" : volume,
            "Capital" : capital,
            "Valorisation" : valorisation,
            "limite hausse" : lim_hausse,
            "limite baisse" : lim_baisse,
            "Rendement" : rendement,
            "PER" : per,
            "Dividende net par action 2022" : dividende_2022,
            "Dividende net par action ESTIM. 2023" : dividende_2023,
            "Dividende net par action ESTIM. 2024" : dividende_2024,
            "Rendement 2022" : rendement_2022,
            "Rendement 2023" : rendement_2023,
            "Rendement 2024" : rendement_2024,
            "Bénéfice net par action 2022" : benefice_2022,
            "Bénéfice net par action 2023" : benefice_2023,
            "Bénéfice net par action 2024" : benefice_2024,
            "PER 2022" : per_2022,
            "PER 2023" : per_2023,
            "PER 2024" : per_2024
            }
        
            
        df = pd.DataFrame(dict)
        link = "orange"
        df.to_csv(str(link)+".csv")
        return link

    def ping(a):

        url = a

        try:
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                print('Le statut de la page web est OK.')
            else:
                print('Le statut de la page web est incorrect.')
        except:
            print('L\'url n\'est pas valide.')

    def find_link():
        link = []
        # on commence par ouvrir le fichier texte
        with open('source_html.txt', 'r', encoding="UTF-8") as f:
            # on parcourt chaque ligne du fichier 
            for line in f:
                # on sépare chaque élément de la ligne
                words = line.split()
                # on parcourt chaque mot de la ligne
                for word in words:
                    # on vérifie si le mot commence par href="/cours/
                    if word.startswith('href="/cours/'):
                        # on affiche le mot
                        link.append(word)

        link = ' '.join(link)
        link = link.split('href="')
        link = ' '.join(link)
        link = link.split(' ')
        link = ' '.join(link)
        link = link.split('"')
        for element in link:
            if element == "":
                link.remove(element)
        link = ' '.join(link)
        link = link.split(" ")
        for element in link:
            if element == '' or element == ">":
                link.remove(element)
        link_clean = []
        for element in link:
            if element != "":
                link_clean.append(element)

        return link_clean

if __name__ == "__main__":
    sp.world.get("https://www.boursorama.com/bourse/actions/cotations/secteur/page-3")
    print(csv.find_link())