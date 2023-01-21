
    '''def limiter(a):
        #on commence par importer le module sys 

        # on définit les variables pour les lignes de départ et d'arrivée 
        start_line = int(evolution.find())
        end_line = int(evolution.find()+a)

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
        del texte_sans_lettres[39:44]
        return texte_sans_lettres'''