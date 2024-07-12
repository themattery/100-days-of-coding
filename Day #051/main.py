from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(self.chrome_options)
        self.down = 0
        self.up = 0
        self.internet_tracker_url = "https://www.speedtest.net/"
        self.twitter_url = "https://x.com/i/flow/login"

    def get_internet_speed(self):
        self.driver.get(self.internet_tracker_url)

        sleep(2)
        privacy_accept = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        privacy_accept.click()

        sleep(2)
        start_button = self.driver.find_element(By.CSS_SELECTOR, value="div.start-button span.start-text")
        start_button.click()

        sleep(10)
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(f"Down: {self.down.text}")
        print((f"Up: {self.up.text}"))
        sleep(5)

    def tweet_at_provider(self):
        self.driver.get(self.twitter_url)
        sleep(10)
        email_input = self.driver.find_element(By.CSS_SELECTOR, value='input[name="text"]')
        email_input.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div/button[2]/div/span/span')
        next_button.click()
        sleep(3)
        password_input = self.driver.find_element(By.CSS_SELECTOR, value='input[name="password"]')
        sleep(3)
        password_input.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        sleep(2)
        tweet_input = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet = f"Hey, ISP, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_input.send_keys(tweet)

