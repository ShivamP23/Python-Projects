import smtplib
import datetime as dt
import random

my_email = "shiv.coding.projects@gmail.com"
password = ""#Enter your password here

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open(r"projects\Automated-Monday-Motivational\Motivational-Quotes\quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)


    with smtplib.SMTP("smtp.gmail.com", 587) as connection: #587 is the port number which helps to connect and send mails. 
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs= "shivampro23@gmail.com", 
                            msg=f"Subject:Monday Motivation\n\n {quote}")
        connection.close()