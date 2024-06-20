# Detects ISS aproximation and sends an email if it's overhead
from datetime import datetime
from tkinter import messagebox
import requests
import smtplib

MY_EMAIL = "example@gmail.com"
MY_PASSWORD = "password"
to_email = "example_destiny@gmail.com"

MY_LAT = -10.119496
MY_LONG = -30.845013

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    # and it is currently dark
    if time_now.hour >= sunset:
        # Then email me to tell me to look up.
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=to_email,
                    msg=f"Subject:ISS is near you!\n\nLook at the sky!")
            messagebox.showinfo(title="Alert", message="Email was sent.")
        except:
            messagebox.showinfo(title="Alert", message="Email was sent.")
