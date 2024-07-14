from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

TARGET_ACCOUNT = "kabooktv"
USERNAME = "ozfordfella"
PASSWORD = "matheus10b#aurora"


class InstaFollower:

    def __init__(self):
        self.url = "https://www.instagram.com"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get(f"{self.url}/accounts/login/")
        sleep(5)
        email_input = self.driver.find_element(By.CSS_SELECTOR, value='input[name="username"]')
        email_input.send_keys(USERNAME)
        sleep(2)
        password_input = self.driver.find_element(By.CSS_SELECTOR, value='input[name="password"]')
        password_input.send_keys(PASSWORD, Keys.ENTER)
        sleep(5)
        deny_notifications = self.driver.find_element(By.XPATH, value='//div[contains(text(), "Agora não")]')
        deny_notifications.click()
        sleep(5)
        decline_popup = self.driver.find_element(By.XPATH, value='//button[contains(text(), "Agora não")]')
        decline_popup.click()

    def find_followers(self):
        self.driver.get(f"{self.url}/{TARGET_ACCOUNT}/")
        sleep(3)
        followers_btn = self.driver.find_element(By.CSS_SELECTOR, value=F'a[href="/{TARGET_ACCOUNT}/followers/"]')
        followers_btn.click()
        sleep(3)
        for _ in range(2):
            self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[3]/div/button').send_keys(Keys.PAGE_DOWN)
            sleep(3)

    def follow(self):
        buttons = self.driver.find_elements(By.XPATH, value='//button[contains(text(), "Seguir")]')
        for button in buttons:
            try:
                button.click()
                sleep(1.2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancelar')]")
                cancel_button.click()


# .send_keys(Keys.END)

bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()

