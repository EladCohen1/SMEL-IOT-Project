import time
import random
import requests

# Replace with your ThingSpeak API Key and Field ID
api_key = ""
field_id = "1"

url = f"https://api.thingspeak.com/update?api_key={api_key}"

while True:
    gas_level = random.uniform(85.0, 400.0)  # Simulate gas level
    payload = {field_id: gas_level}
    response = requests.post(url, data=payload)
    print(f"Data sent to ThingSpeak: {response.status_code}")
    time.sleep(5)  # Send data every 5 seconds
