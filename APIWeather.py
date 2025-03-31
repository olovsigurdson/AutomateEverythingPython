import requests

api_key = '4ca5ac683f50b267fd6a25b6ff39741e'
lat = '64.7502'
lon = '20.9509'

respond = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}')
json_content = respond.json()

for i in range(len(json_content["list"])):

    weather_concat = f'{json_content["city"]["name"]}, {json_content["list"][i]["dt_txt"]}, {json_content["list"][i]["main"]["temp"]}, {json_content["list"][i]["weather"][0]["description"]} \n'

    with open(f"data.txt", "a") as file_temp:
        file_temp.write(weather_concat)
