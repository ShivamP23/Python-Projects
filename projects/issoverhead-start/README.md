# ISS Overhead Notifier

This is a simple Python script that notifies you via email when the International Space Station (ISS) is overhead and it’s nighttime in your location.

## How It Works

1. **ISS Location**: The script checks the current position of the ISS using the Open Notify API.
2. **Nighttime Check**: It then checks if it is currently nighttime based on your location using the Sunrise-Sunset API.
3. **Email Notification**: If both conditions are met (the ISS is overhead and it's nighttime), it sends an email to your Gmail address informing you that the ISS is visible in the sky.

## Setup

1. Clone or download this script to your local machine.
2. Make sure you have the necessary Python modules installed:
   - `requests`
   - `smtplib`
   - `datetime`
   - `time`

   You can install the required modules using:
   ```bash
   pip install requests
## Things to do:
- Edit the following in the script:
- my_email: Replace it with your email address.
- password: Use your Gmail app password. For better security, consider using a more secure method (like OAuth2) instead of storing your password directly in the script.
- MY_LAT and MY_LONG: Set these to your location's latitude and longitude.