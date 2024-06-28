import os
from dotenv import load_dotenv
import requests
from datetime import timedelta, datetime

load_dotenv()

ORIGIN_IATA_CODE = "LON"
IATA_ENDPOINT = os.getenv("AMADEUS_IATA_ENDPOINT")
TOKEN_ENDPOINT = os.getenv("AMADEUS_TOKEN_ENDPOINT")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def get_iata_code(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )
        try:
            iata_code = response.json()['data'][0]['iataCode']
        except IndexError:
            print(f"IndexError: Could not find the IATA code for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: Could not find the IATA code for {city_name}")
            return "Not Found"

        return iata_code

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Full token: {response.json()}\n")
        print(f"Your token: {response.json()['access_token']}")
        print(f"Token expires in: {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_flight_offers(self, destination_iata_code):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        in_six_months = (datetime.now() + timedelta(days=(6 * 30))).strftime("%Y-%m-%d")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": ORIGIN_IATA_CODE,
            "destinationLocationCode": destination_iata_code,
            "departureDate": tomorrow,
            "returnDate": in_six_months,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }
        flight_search_endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        response = requests.get(url=flight_search_endpoint,
                                headers=headers,
                                params=query)
        return response.json()
