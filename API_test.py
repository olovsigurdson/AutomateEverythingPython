import requests
import time
import json
headers = {
    "Authorization": "Discogs token=TwZcHBLEJoENWBHJHQTNthqJqPwGwrFNtHeJPNPH"
}

response = requests.get(url="https://api.discogs.com/users/danspojken/collection/folders/0/releases", headers=headers)

time.sleep(1)


# Check if the response is successful
if response.status_code == 200:
    # Load the JSON content and pretty-print it
    collection = response.json()
    pretty_json = json.dumps(collection, indent=4)
    print(pretty_json)
else:
    print(f"Error: {response.status_code}, {response.text}")