import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from pprint import pprint
import lxml

load_dotenv()

PRODUCT_URL = os.getenv("PRODUCT_URL")

headers = {
    "User-Agent": "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = requests.get(
    url=PRODUCT_URL,
    headers=headers,
)
amazon_webpage = response.content

soup = BeautifulSoup(amazon_webpage, "lxml")
pprint(soup)

price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_float = float(price_without_currency)
print(price_float)
