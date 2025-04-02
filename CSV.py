import pandas as pd

# Définir les en-têtes personnalisés
headers = [
    "Type d'identifiant PP", "Identifiant PP", "Identification nationale PP", "Code civilité d'exercice", 
    "Libellé civilité d'exercice", "Code civilité", "Libellé civilité", "Nom d'exercice", "Prénom d'exercice", 
    "Code profession", "Libellé profession", "Code catégorie professionnelle", "Libellé catégorie professionnelle", 
    "Code type savoir-faire", "Libellé type savoir-faire", "Code savoir-faire", "Libellé savoir-faire", 
    "Code mode exercice", "Libellé mode exercice", "Numéro SIRET site", "Numéro SIREN site", 
    "Numéro FINESS site", "Numéro FINESS établissement juridique", "Identifiant technique de la structure", 
    "Raison sociale site", "Enseigne commerciale site", "Complément destinataire (coord. structure)", 
    "Complément point géographique (coord. structure)", "Numéro Voie (coord. structure)", 
    "Indice répétition voie (coord. structure)", "Code type de voie (coord. structure)", 
    "Libellé type de voie (coord. structure)", "Libellé Voie (coord. structure)", 
    "Mention distribution (coord. structure)", "Bureau cedex (coord. structure)", 
    "Code postal (coord. structure)", "Code commune (coord. structure)", "Libellé commune (coord. structure)", 
    "Code pays (coord. structure)", "Libellé pays (coord. structure)", "Téléphone (coord. structure)", 
    "Téléphone 2 (coord. structure)", "Télécopie (coord. structure)", "Adresse e-mail (coord. structure)", 
    "Code Département (structure)", "Libellé Département (structure)", "Ancien identifiant de la structure", 
    "Autorité d'enregistrement", "Code secteur d'activité", "Libellé secteur d'activité", "Code section tableau pharmaciens", 
    "Libellé section tableau pharmaciens", "Code rôle", "Libellé rôle", "Code genre activité", "Libellé genre activité"
]

# Charger le fichier texte
file_path = r'C:\Users\hugop\Documents\projetSalome\output.txt'  # Remplacez par le chemin de votre fichier

# Lire le fichier avec le séparateur '|'
df = pd.read_csv(file_path, sep='|', encoding='utf-8', header=None)

# Assigner les en-têtes personnalisés
df.columns = headers

# Exporter le DataFrame en fichier Excel
excel_file_path = 'sortie.xlsx'  # Remplacez par le chemin de sortie souhaité
df.to_excel(excel_file_path, index=False)

print(f"Le fichier Excel a été créé : {excel_file_path}")
