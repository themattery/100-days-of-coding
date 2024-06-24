# Habit Tracking using Pixel
# Reminder: create an user UI with Tkinter

import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "example"
GRAPH_ID = "graph_id_here"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Page",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Creating a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
FORMATTED_DATE = today.strftime("%Y%m%d")

pixel_config = {
    "date": FORMATTED_DATE,
    "quantity": "90",
}

# Adding a pixel (day streak) to the graph
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_pixel_config = {
    "quantity": "45",
}

update_pixel_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{FORMATTED_DATE}"

# Updating a pixel
# response = requests.put(url=update_pixel_url, json=update_pixel_config, headers=headers)
# print(response.text)

# Deleting a pixel
r = requests.delete(url=update_pixel_url, headers=headers)
print(r.text)