import requests
from bs4 import BeautifulSoup
import pandas as pd

# Exemple d'URL (à ajuster selon vos critères de recherche)
url = 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=Psychologue&ou=Moselle+%2857%29&univers=pagesjaunes&idOu='
# Envoyer une requête GET pour récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver les éléments contenant les informations sur les praticiens
results = []

# Extraire le nom et l'adresse des psychologues
for item in soup.find_all('h3', {'kameleoonlistener-ovxt': 'true'}):
    # Le nom du psychologue est dans la balise <h3>
    name = item.text.strip()
    
    # L'adresse et le lien vers la carte sont dans la balise <a> juste après
    address_tag = item.find_next('a', {'class': 'pj-lb pj-link'})
    
    # Extraire l'adresse et la valeur du lien pour la carte
    if address_tag:
        address = address_tag.text.strip()
        link = address_tag['href']
    else:
        address = 'N/A'
        link = 'N/A'
    
    # Ajouter les informations dans la liste des résultats
    results.append({'Name': name, 'Address': address, 'Link': link})

# Convertir les résultats en DataFrame pour une meilleure lisibilité
df = pd.DataFrame(results)

# Afficher les résultats
print(df)

# Sauvegarder dans un fichier CSV si nécessaire
df.to_csv('pages_jaunes_psychologues.csv', index=False)
