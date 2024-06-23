# Checks the weather - if it's gonna rain, sends a whatsapp warning
import requests
import os
from twilio.rest import Client

account_sid = 'example'
auth_token = os.environ.get("AUTH_TOKEN")

ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather?'
APPID = os.environ.get("OWM_API_KEY")

MY_LAT = -7.119496
MY_LONG = -34.845013

forecast_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": APPID,
    "cnt": 4,
}

response = requests.get(ENDPOINT, params=forecast_params)
response.raise_for_status()

forecast_data = response.json()

weather_id = forecast_data['weather'][0]['id']
weather_desc = forecast_data['weather'][0]['description']

will_rain = False

if weather_id < 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+{number}',
        body="It's gonna rain today, darling, take your umbrella ☂️",
        to='whatsapp:+{number}',
    )
    print(message.status)

print(f"Weather ID: {weather_id}\nDescription: {weather_desc}")
