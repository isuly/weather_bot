import requests

from app.config import APP_ID


class WeatherForecast:

    def __init__(self, city="Kazan"):
        self.city = city

    def get_current_weather(self):
        response = requests.get("http://api.openweathermap.org//data/2.5/weather",
                                params={'q': self.city, 'APPID': APP_ID})
        if response.status_code == 200:
            return f"Current temperature is {int(response.json()['main']['temp'] - 273)}°C"

    def get_weather_forecast(self):
        response = requests.get("http://api.openweathermap.org//data/2.5/forecast",
                                params={'q': self.city, 'APPID': APP_ID}).json()
        weather_forecast = []
        for forecast in response['list']:
            weather_forecast.append([forecast['dt_txt'], f"+{forecast['main']['temp'] - 273}"])
        return weather_forecast
