import pandas as pd
import re

# Charger le fichier texte avec un séparateur '|'
file_path = "C:/Users/hugop/Downloads/PS_LibreAcces_202504020841\PS_LibreAcces_Personne_activite_202504020841.txt"

# Ouvrir le fichier et remplacer les séparateurs multiples par un seul '|'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    # Remplacer les multiples '|' par un seul '|'
    content = re.sub(r'\|+', '|', content)

# Sauvegarder le contenu nettoyé dans un nouveau fichier temporaire
cleaned_file_path = 'cleaned_file.txt'
with open(cleaned_file_path, 'w', encoding='utf-8') as file:
    file.write(content)

# Lire le fichier nettoyé dans un DataFrame pandas
df = pd.read_csv(cleaned_file_path, sep='|', encoding='utf-8')

# Exporter le DataFrame en fichier Excel
excel_file_path = 'sortie.xlsx'  # Remplacez par le chemin de sortie souhaité
df.to_excel(excel_file_path, index=False)

print(f"Le fichier Excel a été créé : {excel_file_path}")
