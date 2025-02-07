# Workout Tracker

This is a simple Python script that tracks your workouts and logs them in a Google Sheet using the Nutritionix API and Sheety API.

## How It Works
- You enter the exercises you did.
- The script sends the input to the Nutritionix API, which figures out details like calories burned and duration.
- The results are then sent to your Google Sheet using Sheety.
- Your workout gets logged automatically!

## Setup
1. **Get API Keys**
   - Sign up at [Nutritionix](https://www.nutritionix.com/) and get your **APP_ID** and **API_KEY**.
   - Sign up at [Sheety](https://sheety.co/) and create a project to get your **Sheety Authorization Token**.

2. **Update the Script**
   - Replace `APP_ID` and `API_KEY` with your actual Nutritionix API credentials.
   - Replace `sheet_endpoint` with your own Google Sheet API URL from Sheety.

3. **Run the Script**
   - Open a terminal and run:
     ```sh
     python your_script.py
     ```
   - Enter the exercises you did, and your workout will be logged!

## Requirements
- Python 3
- `requests` library (install it with `pip install requests`)

## Notes
- Make sure your API keys and Sheety authorization are correct.
- Update your Sheety URL to match your own sheet.
- This script is just a simple way to log workouts—feel free to improve it!

### Enjoy tracking your workouts! 💪

