import csv

#On définit une liste d'éléments
liste = ["Bob", "Alice", "John", "Paul"]

#On ouvre un fichier csv en écriture
with open("liste.csv", "w") as fichier:
    #On utilise le module csv pour écrire chaque élément de la liste dans une ligne du fichier
    csv_writer = csv.writer(fichier, delimiter=",")
    for element in liste:
        csv_writer.writerow([element])

#On demande à l'utilisateur s'il souhaite ajouter un nouvel élément à la liste
ajouter = input("Voulez-vous ajouter un élément à la liste ? (oui/non) ")

#Tant que l'utilisateur répond oui, on ajoute un élément
while ajouter == "oui":
    #On demande à l'utilisateur de saisir un nouvel élément
    nouvel_element = input("Saisissez l'élément à ajouter à la liste : ")
    #On ajoute l'élément à la liste
    liste.append(nouvel_element)
    #On ouvre le fichier csv en mode ajout
    with open("liste.csv", "a") as fichier:
        #On écrit le nouvel élément dans une nouvelle ligne du fichier
        csv_writer = csv.writer(fichier, delimiter=",")
        csv_writer.writerow([nouvel_element])
    #On demande à l'utilisateur s'il souhaite ajouter un autre élément
    ajouter = input("Voulez-vous ajouter un autre élément à la liste ? (oui/non) ")

#Une fois que l'utilisateur a fini d'ajouter des éléments, on affiche la liste complète
print("La liste complète est :")
print(liste)