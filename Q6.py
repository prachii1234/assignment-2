import pandas as pd
import requests
import time

data = []

url = "http://api.open-notify.org/iss-now.json"

while len(data) < 100:
    response = requests.get(url)
    
    if response.status_code == 200:
        iss_data = response.json()
        
        timestamp = iss_data["timestamp"]
        latitude = iss_data["iss_position"]["latitude"]
        longitude = iss_data["iss_position"]["longitude"]
        
        data.append({"Timestamp": timestamp, "Latitude": latitude, "Longitude": longitude})
        
        time.sleep(1)
    else:
        print("Error:", response.status_code)
        break

df = pd.DataFrame(data)

df.to_csv("iss_location.csv", index=False)

print("Data written to iss_location.csv")