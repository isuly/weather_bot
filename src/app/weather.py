import requests
from pytemperature import k2c

from app.config import APP_ID


class WeatherForecast:

    def __init__(self, city="Kazan"):
        self.city = city

    def get_current_weather(self):
        response = requests.get("http://api.openweathermap.org//data/2.5/weather",
                                params={'q': self.city, 'APPID': APP_ID})
        if response.status_code == 200:
            return f"Current temperature is {int(k2c(response.json()['main']['temp']))}°C"

    def get_weather_forecast(self):
        response = requests.get("http://api.openweathermap.org//data/2.5/forecast",
                                params={'q': self.city, 'APPID': APP_ID}).json()
        weather_forecast = {}
        for forecast in response['list']:
            if forecast['dt_txt'].split(' ')[0] in weather_forecast:
                weather_forecast[forecast['dt_txt'].split(' ')[0]].append(
                    [forecast['dt_txt'].split(' ')[1], f"{int(k2c(forecast['main']['temp']))}°C"])
            else:
                weather_forecast.update({
                    forecast['dt_txt'].split(' ')[0]:
                        [[forecast['dt_txt'].split(' ')[1], f"{int(k2c(forecast['main']['temp']))}°C"]]})
        weather_string = ""
        for dates in weather_forecast.keys():
            weather_string += f"{dates}:\n"
            temperature_string = ""
            for weather in weather_forecast[dates]:
                temperature_string += f"{' '*25}{weather[0]}: {weather[1]}\n"
            weather_string += temperature_string
        return weather_string
