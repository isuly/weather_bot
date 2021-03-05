import requests

from src.config import config


class WeatherForecast:

    def __init__(self, city="Kazan"):
        self.city = city

    def get_current_weather(self):
        response = requests.get("http://api.openweathermap.org//data/2.5/weather",
                                params={'q': self.city, 'APPID': config['weather']['app_id']})
        if response.status_code == 200:
            return f"Current temperature is {int(response.json()['main']['temp'] - 273)}°C"
