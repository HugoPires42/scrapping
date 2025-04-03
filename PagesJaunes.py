import requests
from bs4 import BeautifulSoup
import pandas as pd

# Exemple d'URL (à ajuster selon vos critères de recherche)
url = 'https://www.pagesjaunes.fr/recherche/'

# Envoyer une requête GET pour récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver les éléments contenant les informations sur les praticiens
results = []
for item in soup.find_all('div', class_='bi-bloc'):  # La classe à ajuster en fonction de la structure du site
    name = item.find('a', class_='denomination').text.strip() if item.find('a', class_='denomination') else 'N/A'
    address = item.find('p', class_='adresse').text.strip() if item.find('p', class_='adresse') else 'N/A'
    phone = item.find('p', class_='numero').text.strip() if item.find('p', class_='numero') else 'N/A'
    
    results.append({'Name': name, 'Address': address, 'Phone': phone})

# Convertir les résultats en DataFrame pour une meilleure lisibilité
df = pd.DataFrame(results)

# Afficher les résultats
print(df)

# Sauvegarder dans un fichier CSV si nécessaire
df.to_csv('pages_jaunes_psychologues.csv', index=False)

