from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  

driver.get("https://desafio-geo.vercel.app/")

try:
  
    cidade_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cidade"))
    )
    cidade_input.send_keys("Campinas")

    
    consultar_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "consultar"))
    )
    consultar_button.click()

    
    WebDriverWait(driver, 10).until(
        EC.url_contains("Campinas")
    )

    
    print("URL atual:", driver.current_url)

finally:
   
    driver.quit()
