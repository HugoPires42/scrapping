# Définir les en-têtes (clés) pour les dictionnaires
headers = [
    "Type d'identifiant PP", "Identifiant PP", "Identification nationale PP", 
    "Code civilité d'exercice", "Libellé civilité d'exercice", "Code civilité", 
    "Libellé civilité", "Nom d'exercice", "Prénom d'exercice", "Code profession", 
    "Libellé profession", "Code catégorie professionnelle", "Libellé catégorie professionnelle", 
    "Code type savoir-faire", "Libellé type savoir-faire", "Code savoir-faire", 
    "Libellé savoir-faire", "Code mode exercice", "Libellé mode exercice", 
    "Numéro SIRET site", "Numéro SIREN site", "Numéro FINESS site", 
    "Numéro FINESS établissement juridique", "Identifiant technique de la structure", 
    "Raison sociale site", "Enseigne commerciale site", 
    "Complément destinataire (coord. structure)", "Complément point géographique (coord. structure)", 
    "Numéro Voie (coord. structure)", "Indice répétition voie (coord. structure)", 
    "Code type de voie (coord. structure)", "Libellé type de voie (coord. structure)", 
    "Libellé Voie (coord. structure)", "Mention distribution (coord. structure)", 
    "Bureau cedex (coord. structure)", "Code postal (coord. structure)", 
    "Code commune (coord. structure)", "Libellé commune (coord. structure)", 
    "Code pays (coord. structure)", "Libellé pays (coord. structure)", 
    "Téléphone (coord. structure)", "Téléphone 2 (coord. structure)", 
    "Télécopie (coord. structure)", "Adresse e-mail (coord. structure)", 
    "Code Département (structure)", "Libellé Département (structure)", 
    "Ancien identifiant de la structure", "Autorité d'enregistrement", 
    "Code secteur d'activité", "Libellé secteur d'activité", 
    "Code section tableau pharmaciens", "Libellé section tableau pharmaciens", 
    "Code rôle", "Libellé rôle", "Code genre activité", "Libellé genre activité", 
    "", # Enlever ce dernier header si fichier 1 - fichier 2 ne fonctionne pas à cause du nombre de colonnes
]

# Définir les départements à filtrer
departements_vise = ['88', '57', '54']  # Vosges (88), Moselle (57), Meurthe-et-Moselle (54)

# Fonction pour charger le fichier et créer la liste d'objets
def load_data(file_path):
    # Liste pour stocker les dictionnaires
    data = []
    
    # Ouvrir le fichier texte
    with open(file_path, 'r', encoding='utf-8') as file:
        # Lire chaque ligne du fichier
        lines = file.readlines()

        # Pour chaque ligne dans le fichier
        for line in lines:
            # Enlever les espaces blancs autour de la ligne et la séparer par le délimiteur '|'
            values = line.strip().split('|')
            
            # Vérifier si le nombre de valeurs correspond à celui des en-têtes
            if len(values) == len(headers):
                # Créer un dictionnaire avec les en-têtes comme clés et les valeurs comme valeurs
                record = dict(zip(headers, values))
                
                # Vérifier si le "Code Département (structure)" commence par un des départements visés
                code_departement = record.get("Code Département (structure)")
                if any(code_departement.startswith(dept) for dept in departements_vise):
                    # Ajouter ce dictionnaire à la liste
                    data.append(record)
            else:
                # Si les valeurs ne correspondent pas, afficher un message d'erreur
                print(f"Erreur: La ligne suivante n'a pas le bon nombre de colonnes : {line}")
    
    return data

# Spécifier le chemin vers votre fichier texte
file_path = r'C:\Users\hugop\Documents\projetSalome\data.txt'  # Remplacez par le chemin de votre fichier

# Charger les données depuis le fichier
data = load_data(file_path)

# Afficher les données filtrées
for obj in data:
    print(obj)
