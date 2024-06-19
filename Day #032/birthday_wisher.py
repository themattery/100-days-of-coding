##################### Birthday Email Wisher Project ######################
import datetime as dt
import pandas
import random
import smtplib

EMAIL = "example@gmail.com"
PASSWORD = "password"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

for person in data_dict:
    birth_tuple = (person['month'], person['day'])
    # 2. Check if today matches a birthday in the birthdays.csv
    if today_tuple == birth_tuple:
        name = person['name'].title()
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter_num = random.randint(1, 3)
        with open(f"./letter_templates/letter_{letter_num}.txt") as letter_file:
            letter = letter_file.read()
            letter = letter.replace('[NAME]', name)
            print(letter)

            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="example_receiver@gmail.com",
                    msg=f"Subject:HAPPY BIRTHDAY\n\n{letter}"
                )
