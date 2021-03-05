import requests


class WeatherForecast:

    def __init__(self, city="Kazan"):
        self.city = city

    def get_current_weather(self):
        response = requests.get("http://api.openweathermap.org//data/2.5/weather",
                                params={'q': self.city, 'APPID': '144a633e68a82d00dbecdd5e53d01104'})
        if response.status_code == 200:
            return f"Current temperature is {int(response.json()['main']['temp'] - 273)}°C"
