import requests
from bs4 import BeautifulSoup


class BillboardManager:

    def __init__(self):
        self.chosen_year = input("Which year do you want to travel to? (YYYY-MM-DD)")
        self.BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{self.chosen_year}/"
        self.response = requests.get(self.BILLBOARD_URL)
        self.billboard_html = self.response.text
        self.soup = BeautifulSoup(self.billboard_html, "html.parser")

    def get_songs(self):
        titles = self.soup.select(selector="li h3.c-title")
        all_songs = [title.text.strip() for title in titles]
        return all_songs
