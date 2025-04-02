from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def scrape_psychologues_lorraine():
    url = "https://annuaire.sante.fr/web/site-pro/recherche/rechercheDetaillee"
    driver = webdriver.Chrome()  # Assure-toi d'avoir installé chromedriver
    driver.get(url)
    
    time.sleep(3)  # Attendre le chargement de la page
    
    # Sélection de la profession "Psychologue"
    select_profession = Select(driver.find_element(By.ID, "Profession"))
    select_profession.select_by_visible_text("Psychologue")

    # Sélection de la région "Lorraine"
    select_region = Select(driver.find_element(By.ID, "Region"))
    select_region.select_by_visible_text("Lorraine")

    # Lancer la recherche
    submit_buttons = driver.find_elements(By.CLASS_NAME, "champ_submit")
    submit_buttons[1].click() 
    
    time.sleep(5)  # Attendre le chargement des résultats
    
    # Liste des résultats
    all_results = []
    
    # Récupérer les résultats de chaque page
    while True:
        # Extraction des résultats de la page actuelle
        practitioners = driver.find_elements(By.CLASS_NAME, "contenant_resultat")
        for practitioner in practitioners:
            # Extraire le nom
            name_element = practitioner.find_element(By.CLASS_NAME, "nom_prenom")
            name = name_element.text.strip() if name_element else "Non disponible"
            
            # Extraire l'adresse
            address_element = practitioner.find_element(By.CLASS_NAME, "adresse")
            address = address_element.text.strip() if address_element else "Non disponible"
            
            # Extraire le téléphone
            phone_element = practitioner.find_element(By.CLASS_NAME, "tel")
            phone = phone_element.text.strip() if phone_element else "Non disponible"
            
            all_results.append({
                "Nom": name,
                "Adresse": address,
                "Téléphone": phone
            })
        
        # Vérifier si le bouton "Suivant" est présent et cliquable
        try:
            next_button = driver.find_element(By.CLASS_NAME, "bt_suivant").find_element(By.TAG_NAME, "a")
            if next_button:
                next_button.click()  # Clique sur "Suivant"
                time.sleep(5)  # Attendre que la nouvelle page se charge
            else:
                break  # Si le bouton n'est pas trouvé, arrêter le scraping
        except:
            break  # Si une exception se produit (par exemple, si le bouton n'est plus présent), arrêter
    
    driver.quit()
    return all_results

# Exécution du script
psychologues = scrape_psychologues_lorraine()
for p in psychologues:
    print(p)
