import json
import requests
API_KEY = "a2eba7bd0a077eb3f8f28bcecb12e3a4"
hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = f"http://api.openweathermap.org/geo/1.0/direct?q={hakusana}&limit=1&appid={API_KEY}"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        json_vastaus = vastaus.json()
        for vastaus in json_vastaus:
            lat = vastaus["lat"]
            lon = vastaus["lon"]
        pyyntö = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        vastaus = requests.get(pyyntö)
        json_vastaus = vastaus.json()
        kelvin = json_vastaus["main"]["temp"]
        print(f"{kelvin - 273.15:.02f}")
except:
    print ("säätä ei enää ole....")