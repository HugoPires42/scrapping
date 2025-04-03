from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialiser le WebDriver (ici avec Chrome)
driver = webdriver.Chrome()

# Accéder à la page des Pages Jaunes
driver.get("https://www.pagesjaunes.fr/")

# Attendre que le pop-up de cookies soit présent et accepter
try:
    # Attendre que le bouton d'acceptation des cookies soit cliquable
    wait = WebDriverWait(driver, 10)
    accept_button = wait.until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button")))
    accept_button.click()  # Cliquer pour accepter les cookies
    print("Cookies acceptés.")
    time.sleep(1)  # Attendre un peu pour s'assurer que le pop-up est fermé
except Exception as e:
    print(f"Erreur lors de l'acceptation des cookies : {e}")

# Trouver le champ pour "quoi" (Psychologue)
quoi_field = driver.find_element(By.ID, "quoiqui")
quoi_field.send_keys("psychologue")  # Renseigner "psychologue"

# Trouver le champ pour "où" (Lorraine)
ou_field = driver.find_element(By.ID, "ou")
ou_field.send_keys("Lorraine")  # Renseigner "Lorraine"

# Attendre que le bouton "Trouver" soit cliquable
wait = WebDriverWait(driver, 10)
find_button = wait.until(EC.element_to_be_clickable((By.ID, "findId")))

# Cliquer sur le bouton "Trouver"
find_button.click()

# Attendre un peu pour voir le résultat de la recherche
time.sleep(5)

# Trouver et cliquer sur le lien "Lorraine"
try:
    # Attendre que le lien "Lorraine" soit cliquable
    lorraine_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Lorraine']")))
    lorraine_link.click()
    print("Lien 'Lorraine' cliqué.")
except Exception as e:
    print(f"Erreur lors du clic sur le lien 'Lorraine' : {e}")

# Attendre un peu pour voir les résultats après le clic
time.sleep(5)

# Optionnel : Récupérer le HTML de la page de résultats
html = driver.page_source
print(html)

# Fermer le navigateur
driver.quit()
