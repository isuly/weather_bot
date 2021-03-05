import telebot

from src.config import config
from src.weather import WeatherForecast

bot = telebot.TeleBot(config['bot_id'])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi! Im weather bot! \nSend me "weather" to get current weather!')


@bot.message_handler(content_types=['text'])
def get_current_weather(message):
    if message.text.lower() == 'weather':
        bot.send_message(message.chat.id, 'Send me your city')
    else:
        current_weather = WeatherForecast(city=message.text).get_current_weather()
        bot.send_message(message.chat.id, current_weather)


bot.polling()
