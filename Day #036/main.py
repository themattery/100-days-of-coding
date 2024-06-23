# Stock Trading News Alert Project
# If the stock closing prices from the last 2 days
# fluctuated for over 5%, a phone message is sent.

import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load .env file
load_dotenv(".env")

# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Stock API Constants
STOCK_URL = "https://www.alphavantage.co/query?"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

# News API Constants
NEWS_URL = "https://newsapi.org/v2/everything?"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

# Twilio API Constants
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
TWILIO_PHONE_RECEIVER = os.getenv("TWILIO_PHONE_RECEIVER")

# Getting Stock json from Alpha Vantage API
response = requests.get(STOCK_URL, params=stock_parameters)
data = response.json()["Time Series (Daily)"]

# Getting hold of closing stock prices from yesterday and the day before
data_list = [value for (key, value) in data.items()]
yesterday_close_price = float(data_list[0]["4. close"])
before_yesterday_close_price = float(data_list[1]["4. close"])

# Finding stock percentage change
close_prices_difference = yesterday_close_price - before_yesterday_close_price
percentage_change = round(close_prices_difference * 100 / yesterday_close_price)

# Changing symbol whether stock increased or decreased
if close_prices_difference > 0:
    change_symbol = "🔺"
else:
    change_symbol = "🔻"

# Check if percentage change is at least over 5%
if abs(percentage_change) > 0:
    # Getting 3 main news related to the current stock company
    news_response = requests.get(NEWS_URL, params=news_parameters)
    news_data = news_response.json()
    main_news_data = news_data['articles'][0:3]

    # Creating message with news
    news_message = f"{STOCK}: {change_symbol}{round(percentage_change, 2)}%\n\n"
    for news in main_news_data:
        news_message += f"*Headline:* {news['title']}\n*Brief:* {news['description']}\n\n"

    # Sending message
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=TWILIO_PHONE,
        body=news_message,
        to=TWILIO_PHONE_RECEIVER,
    )

    print(message.sid)

    print(news_message)
