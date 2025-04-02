# Lire le contenu de deux fichiers .txt et extraire les différences
def lire_fichier(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.readlines())  # Utilisation de set pour retirer les doublons et faciliter la comparaison

def trouver_diff(file1_path, file2_path):
    # Lire les contenus des fichiers
    file1_lines = lire_fichier(file1_path)
    file2_lines = lire_fichier(file2_path)

    # Trouver la différence entre les fichiers (lignes dans file2 mais pas dans file1)
    diff = file2_lines - file1_lines
    return diff

def enregistrer_diff(diff, output_file):
    # Enregistrer les lignes de différence dans un nouveau fichier
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(diff)

# Chemins vers les fichiers
file1_path = r"C:\Users\hugop\Downloads\PS_LibreAcces_202504020841\1.txt"  # Remplacez par le chemin de votre premier fichier
file2_path = r"C:\Users\hugop\Downloads\PS_LibreAcces_202504020841\2.txt"  # Remplacez par le chemin de votre second fichier
output_file = r"C:\Users\hugop\Documents\projetSalome  # Chemin pour sauvegarder les différences

# Trouver les différences et les enregistrer dans un fichier
diff = trouver_diff(file1_path, file2_path)
enregistrer_diff(diff, output_file)

print(f"Les différences ont été enregistrées dans : {output_file}")
