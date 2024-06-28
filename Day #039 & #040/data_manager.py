import requests
from dotenv import load_dotenv
import os

load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}
        self._SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
        self._SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = (self._user, self._password)

    def get_sheet_data(self):
        response = requests.get(
            url=self._SHEETY_PRICES_ENDPOINT,
            auth=self._authorization)
        return response.json()['prices']

    def update_sheet(self):
        for row in self.sheet_data:
            body = {
                "price": {
                    "iataCode": row['iataCode']
                }
            }
            response = requests.put(
                url=f"{self._SHEETY_PRICES_ENDPOINT}/{row['id']}",
                json=body,
                auth=self._authorization,
            )

    def get_customer_emails(self):
        response = requests.get(
            url=self._SHEETY_USERS_ENDPOINT,
            auth=self._authorization,
        )
        data = response.json()["users"]
        return data
