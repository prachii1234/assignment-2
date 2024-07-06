import requests
import json

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    iss_position = data["iss_position"]
    print("Latitude:", iss_position["latitude"])
    print("Longitude:", iss_position["longitude"])
    print("Timestamp:", data["timestamp"])
else:
    print("Error:", response.status_code)