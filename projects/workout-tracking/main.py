import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 172
AGE = 21

# APP_ID = your nutritionix id
# API_KEY = and your key from nutritionix key

#also provide your authorization from sheety
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/791388eb0d42ddcfb4d3f88a32c89964/myWorkoutsProject/workouts"
# also change this to your own sheet 
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json= sheet_inputs)

    print(sheet_response.text)

#f9fd6cba
#"35f19250ca2f3e4db812ac7197b8e535"