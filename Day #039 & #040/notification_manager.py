import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
RECEIVER_PHONE_NUMBER = os.getenv("RECEIVER_PHONE_NUMBER")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self._my_email = os.getenv("SMTP_MY_EMAIL")
        self._my_password = os.getenv("SMTP_MY_PASSWORD")

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{TWILIO_PHONE_NUMBER}',
            body=message_body,
            to=f'whatsapp:{RECEIVER_PHONE_NUMBER}'
        )
        print(message.sid)

    def send_emails(self, email_list, message):
        for email in email_list:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self._my_email, password=self._my_password)
                connection.sendmail(
                    from_addr=self._my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
