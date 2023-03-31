# import requests

# API_KEY = "e37d72c86eb111e39d10d562800d7580"
# API_URL = "https://api.openweathermap.org/data/2.5/weather"

# def get_weather(city):
#     query_params = {
#         "q": city,
#         "appid": API_KEY,
#         "units": "metric"
#     }

#     response = requests.get(API_URL, params=query_params)
#     response_json = response.json()

#     if response.status_code == 200:
#         temperature = response_json["main"]["temp"]
#         description = response_json["weather"][0]["description"]
#         print(f"The temperature in {city} is {temperature:.1f}°C")
#         print(f"The description is: {description}")
#     else:
#         print("Unable to retrieve weather information.")

# if __name__ == "__main__":
#     city = input("Enter a city name: ")
#     get_weather(city)

import requests

API_KEY = "e37d72c86eb111e39d10d562800d7580"
API_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city, country=None):
    query_params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    if country:
        query_params["q"] += f",{country}"

    response = requests.get(API_URL, params=query_params)
    response_json = response.json()

    if response.status_code == 200:
        temperature = response_json["main"]["temp"]
        description = response_json["weather"][0]["description"]
        wind_speed = response_json["wind"]["speed"]
        humidity = response_json["main"]["humidity"]
        pressure = response_json["main"]["pressure"]
        print(f"The temperature in {city} is {temperature:.1f}°C with {description}\nwind speed of {wind_speed} m/s\nhumidity of {humidity}%\nand pressure of {pressure} hPa")
    else:
        print("Unable to retrieve weather information.")

def get_forecast(city, country=None):
    query_params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    if country:
        query_params["q"] += f",{country}"

    response = requests.get(FORECAST_URL, params=query_params)
    response_json = response.json()

    if response.status_code == 200:
        forecasts = response_json["list"]
        print("\n-------------------------------------------------")
        print(f"\n5-day weather forecast for {city}:")
        print("\n-------------------------------------------------")
        for forecast in forecasts:
            date = forecast["dt_txt"]
            temperature = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]
            print(f"{date}: {description} with a temperature of {temperature:.1f}°C")
    else:
        print("Unable to retrieve forecast information.")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    country = input("Enter the country code (optional): ")

    get_weather(city, country)
    get_forecast(city, country)
