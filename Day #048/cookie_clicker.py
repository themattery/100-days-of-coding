# Cookie Clicker Project
# Ok, so... basically... it clicks on a giant... cookie.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

cookie = driver.find_element(By.CSS_SELECTOR, value="div#cookie")

timeout = time.time() + 5

money = driver.find_element(By.ID, value="money")
print(money.text)

store = driver.find_elements(By.CSS_SELECTOR, value="#store b")
for item in store:
    print(item.text.split('-')[-1])


timeout = time.time() + 5

while True:
    while time.time() < timeout:
        cookie.click()
        
    store_items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    last_non_grayed = None
    for item in store_items:
        if "grayed" not in item.get_attribute("class"):
            last_non_grayed = item

    if last_non_grayed:
        last_non_grayed.click()

    timeout = time.time() + 5

