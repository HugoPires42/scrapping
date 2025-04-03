from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialiser le WebDriver (ici avec Chrome)
driver = webdriver.Chrome()

# Accéder à la page des Pages Jaunes
driver.get("https://www.pagesjaunes.fr/")

# Attendre un peu que la page se charge
time.sleep(3)

# Trouver le champ pour "quoi" (Psychologue)
quoi_field = driver.find_element(By.ID, "quoiqui")
quoi_field.send_keys("psychologue")  # Renseigner "psychologue"

# Trouver le champ pour "où" (Lorraine)
ou_field = driver.find_element(By.ID, "ou")
ou_field.send_keys("Lorraine")  # Renseigner "Lorraine"

# Trouver et cliquer sur le bouton "Trouver"
find_button = driver.find_element(By.ID, "findId")
find_button.click()

# Attendre un peu pour voir le résultat de la recherche
time.sleep(5)

# Optionnel : Si tu veux récupérer le HTML de la page de résultats
html = driver.page_source
print(html)

# Fermer le navigateur
driver.quit()
