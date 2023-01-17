# Importer les bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup
 
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