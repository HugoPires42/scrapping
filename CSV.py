import pandas as pd

# Charger le fichier texte
file_path = r'C:\Users\hugop\Documents\projetSalome\output.txt'  # Remplacez par le chemin de votre fichier
df = pd.read_csv(file_path, sep='|', encoding='utf-8')

# Exporter le DataFrame en fichier Excel
excel_file_path = 'sortie.xlsx'  # Remplacez par le chemin de sortie souhaité
df.to_excel(excel_file_path, index=False)

print(f"Le fichier Excel a été créé : {excel_file_path}")
