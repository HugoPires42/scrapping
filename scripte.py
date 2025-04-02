from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
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
   search_button = driver.find_element(By.CLASS_NAME, "champ_submit")
    search_button.click()
    
    time.sleep(5)  # Attendre le chargement des résultats
    
    # Extraction des résultats
    results = []
    practitioners = driver.find_elements(By.CLASS_NAME, "result-card")
    
    for practitioner in practitioners:
        name = practitioner.find_element(By.CLASS_NAME, "result-name").text
        address = practitioner.find_element(By.CLASS_NAME, "result-address").text
        phone = practitioner.find_element(By.CLASS_NAME, "result-phone").text if practitioner.find_elements(By.CLASS_NAME, "result-phone") else "Non disponible"
        
        results.append({
            "Nom": name,
            "Adresse": address,
            "Téléphone": phone
        })
    
    driver.quit()
    return results

# Exécution du script
psychologues = scrape_psychologues_lorraine()
for p in psychologues:
    print(p)
