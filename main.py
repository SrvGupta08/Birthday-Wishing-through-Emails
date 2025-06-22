''' Check if today matches a birthday in the birthdays.csv, then pick a random letter from letter templates and replace
the '[NAME]' with the person's actual name from birthdays.csv and send the letter generated to that person's email
address. '''

import smtplib
import datetime as dt
import pandas as pd
import random

MY_EMAIL = "sourav@gmail.com"
MY_PASSWORD = "dsvcjhgjhdgdhggh"

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("./birthdays.csv")
bday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

if today in bday_dict:
    bday_person = bday_dict[today]
    file_path = f"./letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_to_send:
        contents = letter_to_send.read()
        contents = contents.replace("[NAME]", bday_person["name"])


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addrs = bday_person["email"],
            msg = f"Subject:Happy Birthday\n\n{contents}"
        )
