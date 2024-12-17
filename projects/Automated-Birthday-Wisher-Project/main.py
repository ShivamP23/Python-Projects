from datetime import datetime
import pandas
import random
import smtplib

my_email = "shiv.coding.projects@gmail.com"
password = ""#Enter your password here

today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv(r"projects\Automated-Birthday-Wisher-Project\birthdays.csv")
birthdats_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}


if today_tuple in birthdats_dict:
    birthday_person = birthdats_dict[today_tuple]
    file_path = r"projects\Automated-Birthday-Wisher-Project\letter_templates\letter_" + str(random.randint(1, 3)) + ".txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs= birthday_person["email"], 
                            msg=f"Subject: Happy Birthday!\n\n {contents}")
        connection.close()