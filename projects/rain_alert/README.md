# OpenWeatherMap API Forecast Script

This is a simple Python script that fetches weather forecast data using the OpenWeatherMap API and checks if it will rain.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)

## Setup
1. Get an API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys)
2. Replace `api_key` in the script with your actual API key

## How It Works
- **Fetches Weather Data** for a specific location (set to Edison, NJ by default)
- **Checks for Rain** by analyzing weather condition codes
- **Sends a Text Message Reminder** if rain is expected

## Usage
1. Make sure you have your API key set up correctly.
2. Add your phone number to the script where indicated.
3. Run the script:
   ```bash
   python script.py
   ```
4. If rain is detected, the script will send a text message:
   ```
   Bring an umbrella.
   ```

## Notes
- Modify the latitude and longitude values in `weather_params` for a different location.
- The script checks the next 4 forecasted time slots (`cnt=4`). Adjust as needed.
- Make sure to integrate a messaging service like Twilio to send SMS alerts.

## Example Response
If rain is expected, you will receive a text message:
```
Bring an umbrella.
```
Otherwise, no message is sent.



