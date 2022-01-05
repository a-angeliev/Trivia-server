import requests
from decouple import config


class WeatherInfo:
    @staticmethod
    def info():
        headers = {
            "x-api-key": f"{config('WEATHER_API')}",
            "Content-type": "application/json",
        }
        sofia_coor = {"lat": "42.6977", "lng": "23.3219"}
        response = requests.request(
            "GET", config("WEATHER_URL"), headers=headers, params=sofia_coor
        )
        return response.json()["data"]["windSpeed"]
