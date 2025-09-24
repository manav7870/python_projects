#WEATHER APP USING OPENWEATHERAPI

import requests

url = "https://api.openweathermap.org/data/2.5/weather"
key_value = "4c345a720583c15e8b5fa7f34acbc29d"

a = input("Enter your city: ")
param = {
    "q": a,
    "appid" : key_value,
    "units" : "metric"
}

response = requests.get(url, params=param)
if response.status_code == 200:
    data = response.json()
    wind_ms = data['wind']['speed']
    wind_km = wind_ms * 3.6
    print(f"Weather in {a}!\n")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Condition: {data['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {wind_km:.2f}km/s")
else:
    print("City not found or error in fetching data")    