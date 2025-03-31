import requests
import json
url = "https://api.languagetool.org/v2/check"

data_dict = {
    "text": "Can you speak anglish?",
    "language": "auto"
}

response = requests.post(url, data=data_dict)
json_load = json.loads(response.text)
print(json_load)

