from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os

load_dotenv()

URL = os.getenv("JOB_URL")
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(chrome_options)
driver.get(URL)

time.sleep(2)
login_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
login_button.click()

time.sleep(2)
email_input = driver.find_element(By.ID, value="username")
email_input.send_keys(EMAIL)

password_input = driver.find_element(By.ID, value="password")
password_input.send_keys(PASSWORD, Keys.ENTER)

time.sleep(10)
close_popup = driver.find_element(By.ID, value='ember45')
close_popup.click()

time.sleep(2)
jobs = driver.find_elements(By.CSS_SELECTOR, value="ul.scaffold-layout__list-container li.ember-view strong")

jobs[0].click()
for i in range(1, len(jobs)):
    time.sleep(2)
    save_job_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/button')
    save_job_button.click()

    time.sleep(2)
    for _ in range(6):
        save_job_button.send_keys(Keys.PAGE_DOWN)

    time.sleep(2)
    follow_company = driver.find_element(By.CSS_SELECTOR, value="button.follow")
    follow_company.click()
    jobs[i+1].click()
