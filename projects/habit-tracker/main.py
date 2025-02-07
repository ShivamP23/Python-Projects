import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "shivam30"
#TOKEN = "use your own token"
GRAPH_ID = "graph30"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url =pixela_endpoint, json = user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Lift Sesson",
    "unit": "Kg",
    "type": "float",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, json=graph_config, headers= headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()  # Add parentheses to call the function
pixel_data = {
    "date": today.strftime("%Y%m%d"),  # Pixela expects the date in 'YYYYMMDD' format
    "quantity": "25",
}
response = requests.post(url = pixel_creation_endpoint, json= pixel_data, headers= headers)
print(response.text)


# https://pixe.la/@shivam30"
# https://pixe.la/v1/users/shivam30/graphs/graph30.html
#abcdefghim30