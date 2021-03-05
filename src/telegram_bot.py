import telebot

from src.config import config
from src.weather import WeatherForecast

bot = telebot.TeleBot(config['bot_id'])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')


@bot.message_handler(commands=['weather'])
def get_current_weather(message):
    current_weather = WeatherForecast(city="Kazan").get_current_weather()
    bot.send_message(message.chat.id, current_weather)


bot.polling()
