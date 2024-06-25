# Workout Tracker Project
# Uses Nutritionix AI to get workout inputs, and then
# add the info to google sheets using Sheety API

import requests
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

load_dotenv(find_dotenv(".env"))

# CONSTANTS
GENDER = "male"
WEIGHT_KG = 85.5
HEIGHT_CM = 175
AGE = 24

# Nutritionix CONSTANTS
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

HOST_DOMAIN = "https://trackapi.nutritionix.com"
EXERCISE_LANG_ENDPOINT = f"{HOST_DOMAIN}/v2/natural/exercise"

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Sheet CONSTANTS
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")
SHEETY_USER_LINK = os.getenv("SHEETY_USER_LINK")
workout_sheet_endpoint = f"https://api.sheety.co/{SHEETY_USER_LINK}/workoutTracking/workouts"

prompt = input("Tell me about your exercise: ")

parameters = {
    "query": prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=EXERCISE_LANG_ENDPOINT, json=parameters, headers=HEADERS)
all_exercises = response.json()['exercises']

# Date, Time, Exercise, Duration, Calories
now = datetime.now()
formatted_date = now.date().strftime("%d/%m/%Y")
formatted_time = now.time().strftime('%X')

for exercise in all_exercises:
    workout_sheet_parameters = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    # Adding new row to workout sheet
    r = requests.post(url=workout_sheet_endpoint, json=workout_sheet_parameters, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
    print(r.text)
