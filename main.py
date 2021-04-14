import pandas
import random
import smtplib
from datetime import datetime
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")

data_file = pandas.read_csv("birthdays.csv")
data = data_file.to_dict(orient="records")
today = datetime.now()

for person in data:
    if person["month"] == today.month and person["day"] == today.day:
        number = random.randint(1, 3)

        with open(f"letter_templates/letter_{number}.txt") as letter_file:
            letter_template = letter_file.read()
            new_letter = letter_template.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!!\n\n{new_letter}"
            )
