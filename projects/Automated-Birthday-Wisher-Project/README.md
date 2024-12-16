# Automated Birthday Wisher

This is a simple Python script that automatically sends birthday wishes via email. It checks if today is someone's birthday from a CSV file and sends them a personalized email with a random birthday template.

## Features
- Checks birthdays from a CSV file (`birthdays.csv`).
- Sends personalized birthday emails.
- Randomly selects a birthday message template.

## Requirements
- Python 3.x
- `pandas` library (install with `pip install pandas`)
- Gmail account for sending emails

## How It Works
1. The script reads the `birthdays.csv` file.
2. It checks if today matches any birthday.
3. If there's a match, it picks a random birthday template from `letter_templates/`.
4. The email is sent via Gmail’s SMTP server with the recipient's name inserted into the template.

