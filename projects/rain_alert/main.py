import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "fe5e2a81a5857cc18bbc040125649e3a"

weather_params = {
    "lat": 40.518715,
    "lon": -74.412094,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()  # This will raise an error for any status code other than 2xx

weather_data = response.json()  # Get the weather data as JSON
#print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
       