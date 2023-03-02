import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "your path to chrome driver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

game_timeout = time.time() + 1000
purchase_timeout = time.time() + 5

while game_timeout > time.time():
    cookie.click()
    if purchase_timeout < time.time():
        stores = driver.find_elements(By.CSS_SELECTOR, "#store>div")
        stores.reverse()
        for store in stores:
            if store.get_attribute("class") != "grayed":
                store.click()
                purchase_timeout = time.time() + 5
                break

    
driver.quit()
